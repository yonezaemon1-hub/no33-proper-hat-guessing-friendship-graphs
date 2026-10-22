"""Second implementation: direct local tables and intersection of bit masks.

Does not import the exhaustive verifier or read its output. Its literal
rows are transcribed from PROOF.md, then checked against witness.json.
This is a separate implementation by the same assistant, not external review.
"""
import argparse
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def expanded(q, rows):
    # rows[petal][side] is indexed by difference minus one.
    return [[[[ (a + row[(y-a) % q - 1]) % q if y != a else None
                for y in range(q)] for a in range(q)] for row in pair]
            for pair in rows]


def verify_masks(q, rows):
    tables = expanded(q, rows)
    masks = []
    choices = list(itertools.permutations(range(q), 2))
    for petal in tables:
        view_masks = []
        for x, y in choices:
            m = 0
            for a in range(q):
                if a != x and a != y and petal[0][a][y] != x and petal[1][a][x] != y:
                    m |= 1 << a
            view_masks.append(m)
        masks.append(view_masks)
    n = 0
    singles = empty = 0
    for vals in itertools.product(*masks):
        m = (1 << q) - 1
        for v in vals:
            m &= v
        assert m.bit_count() <= 1, (q, vals, m)
        n += 1
        singles += m.bit_count() == 1
        empty += m == 0
    return {'outer_views': n, 'singleton': singles, 'empty': empty,
            'ambiguous': 0}


def first_failure(q, rows):
    tables = expanded(q, rows)
    for ab in itertools.combinations(range(q), 2):
        pairs = []
        for petal in tables:
            witness = next(((x, y) for x, y in itertools.permutations(range(q), 2)
                            if all(a not in (x, y)
                                   and petal[0][a][y] != x
                                   and petal[1][a][x] != y for a in ab)), None)
            if witness is None:
                break
            pairs.append(witness)
        else:
            return {'hub_color_pair': list(ab), 'leaf_pairs': pairs}
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', type=Path)
    args = ap.parse_args()
    cert = json.loads((ROOT/'witness.json').read_text(encoding='utf-8'))
    q5 = [[[2, 4, 4, 3], [3, 3, 1, 1]]]
    q6 = [[[4, 3, 1, 3, 3], [4, 3, 1, 3, 3]],
          [[4, 5, 4, 5, 1], [4, 5, 4, 5, 1]]]
    h = [3, 5, 2, 5, 3, 2]
    # Inverses of 1,2,3 modulo 7 are 1,4,5. Write them explicitly.
    q7 = []
    for d, inverse in ((1, 1), (2, 4), (3, 5)):
        row = [(d * h[(inverse*t) % 7 - 1]) % 7 for t in range(1, 7)]
        q7.append([row[:], row[:]])
    assert cert['F1_q5']['tables'] == [{'left':q5[0][0], 'right':q5[0][1]}]
    assert cert['F2_q6']['tables'] == [{'left':a, 'right':b} for a,b in q6]
    assert cert['F3_q7']['base_table'] == h
    assert cert['F3_q7']['scales'] == [1,2,3]
    result = {f'F{len(rows)}_q{q}': verify_masks(q, rows)
              for q, rows in ((5,q5), (6,q6), (7,q7))}

    # Negative control: remove the third 7-color petal. Produce a common
    # outer view at which two different actual hub colors make all leaves
    # wrong. This demonstrates detection, not a universal 2-petal proof.
    negative = first_failure(7, q7[:2])
    assert negative is not None
    result['negative_control_remove_third_petal'] = negative
    # Negative control: change one legal base-table entry and regenerate
    # every scaled petal. Find a failing legal mutation deterministically.
    found = None
    for index in range(6):
        for replacement in range(1,7):
            if replacement in (index+1,h[index]):
                continue
            changed = h[:]
            changed[index] = replacement
            rows = []
            for d, inverse in ((1,1),(2,4),(3,5)):
                row = [(d*changed[(inverse*t) % 7-1]) % 7 for t in range(1,7)]
                rows.append([row[:],row[:]])
            failure = first_failure(7,rows)
            if failure is not None:
                found = {'difference':index+1, 'old':h[index],
                         'new':replacement, 'counterexample':failure}
                break
        if found:
            break
    assert found
    result['negative_control_legal_table_mutation'] = found
    # Check the small integer counts used in the universal upper proof.
    # These checks support its arithmetic; PROOF.md supplies its logic.
    assert 6*5 > 4*6
    assert 5*4 == 4*5
    assert (7*3)//2 == 10
    assert 2*10 < 7*6//2
    result['upper_bound_arithmetic'] = {
        'q8_pairs':30, 'q8_four_event_capacity':24,
        'q7_pairs':20, 'q7_four_event_capacity':20,
        'q7_max_degree':3, 'q7_max_edges_per_petal':10,
        'two_petal_capacity':20, 'hub_color_pairs':21,
        'note':'Arithmetic checks only; the universal quantifiers are proved in PROOF.md.'}
    text = json.dumps(result, indent=2)
    print(text)
    if args.output:
        args.output.write_text(text+'\n',encoding='utf-8')


if __name__=='__main__':
    main()
