"""Dependency-free verification of the three explicit LOWER bounds.

Python 3.12; run from any working directory. The infinite-family upper
bounds are proved in PROOF.md, not inferred from these finite enumerations.
"""
import argparse
import itertools
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def leaf(case, petal, side, hub, partner):
    q = case['q']
    d = (partner - hub) % q
    if d == 0:
        return 0  # This local view cannot occur in a proper coloring.
    if case['type'] == 'translation_tables':
        row = case['tables'][petal]['left' if side == 0 else 'right']
        return (hub + row[d - 1]) % q
    s = case['scales'][petal]
    index = (pow(s, -1, q) * d) % q
    return (hub + s * case['base_table'][index - 1]) % q


def survivors(case, pairs):
    q = case['q']
    return [a for a in range(q)
            if all(a not in (x, y)
                   and leaf(case, j, 0, a, y) != x
                   and leaf(case, j, 1, a, x) != y
                   for j, (x, y) in enumerate(pairs))]


def pair_graphs(case):
    q, r = case['q'], case['petals']
    graphs = []
    tests = 0
    for j in range(r):
        edges = []
        for a, b in itertools.combinations(range(q), 2):
            covered = True
            for x, y in itertools.permutations(
                    [c for c in range(q) if c not in (a, b)], 2):
                tests += 1
                if not (leaf(case, j, 0, a, y) == x
                        or leaf(case, j, 1, a, x) == y
                        or leaf(case, j, 0, b, y) == x
                        or leaf(case, j, 1, b, x) == y):
                    covered = False
            if covered:
                edges.append((a, b))
        graphs.append(edges)
    covered = {edge for g in graphs for edge in g}
    assert covered == set(itertools.combinations(range(q), 2))
    return graphs, tests


def run_case(label, case):
    q, r = case['q'], case['petals']
    legal_views = 0
    for j in range(r):
        for side in range(2):
            for a, y in itertools.permutations(range(q), 2):
                g = leaf(case, j, side, a, y)
                assert g not in (a, y), (label, j, side, a, y, g)
                legal_views += 1
    graphs, local_tests = pair_graphs(case)
    if label == 'F2_q6':
        assert graphs[0] == [(a, b) for a, b in itertools.combinations(range(q), 2)
                             if (b-a) % q != 3]
        assert graphs[1] == [(a, b) for a, b in itertools.combinations(range(q), 2)
                             if (b-a) % q == 3]
    if label == 'F3_q7':
        for d, g in zip(case['scales'], graphs):
            assert g == [(a, b) for a, b in itertools.combinations(range(q), 2)
                         if (b-a) % q in (d, (-d) % q)]

    # Construct the hub's lookup table using only its visible leaf colors.
    # This construction is performed before testing any actual hub color.
    outer_patterns = list(itertools.permutations(range(q), 2))
    hub_lookup = {}
    survivor_hist = Counter()
    for pairs in itertools.product(outer_patterns, repeat=r):
        rem = survivors(case, pairs)
        assert len(rem) <= 1, (label, pairs, rem)
        survivor_hist[len(rem)] += 1
        unseen = [a for a in range(q) if all(a not in p for p in pairs)]
        hub_lookup[pairs] = rem[0] if rem else (unseen[0] if unseen else 0)

    checked = all_leaves_wrong = failures = 0
    winner_hist = Counter()
    for a in range(q):
        patterns = list(itertools.permutations([c for c in range(q) if c != a], 2))
        for pairs in itertools.product(patterns, repeat=r):
            checked += 1
            leaf_winners = sum(
                (leaf(case, j, 0, a, y) == x)
                + (leaf(case, j, 1, a, x) == y)
                for j, (x, y) in enumerate(pairs))
            all_leaves_wrong += leaf_winners == 0
            winners = leaf_winners + (hub_lookup[pairs] == a)
            winner_hist[winners] += 1
            failures += winners == 0
    assert checked == q * ((q-1) * (q-2)) ** r
    assert failures == 0
    return {
        'status': 'PASS', 'q': q, 'petals': r,
        'legal_leaf_views': legal_views, 'local_pair_tests': local_tests,
        'good_pair_edge_counts': list(map(len, graphs)),
        'outer_views': len(hub_lookup),
        'survivor_count_histogram': dict(sorted(survivor_hist.items())),
        'proper_colorings': checked, 'all_leaves_wrong': all_leaves_wrong,
        'failures': failures,
        'correct_guess_count_histogram': dict(sorted(winner_hist.items())),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', type=Path)
    args = ap.parse_args()
    cert = json.loads((ROOT / 'witness.json').read_text(encoding='utf-8'))
    result = {label: run_case(label, cert[label])
              for label in ('F1_q5', 'F2_q6', 'F3_q7')}
    text = json.dumps(result, indent=2)
    print(text)
    if args.output:
        args.output.write_text(text + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
