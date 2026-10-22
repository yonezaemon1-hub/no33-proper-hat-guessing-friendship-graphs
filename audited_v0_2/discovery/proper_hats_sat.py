"""Exploratory SAT for deterministic proper hat guessing on cycles.

No anonymity, translation invariance, or affine restriction is imposed.
Timeouts return UNKNOWN. A found strategy is checked by fresh enumeration.
"""
import argparse
import itertools
import json
import sys
import threading
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'research_deps'))
from pysat.solvers import Solver


def make_instance(n, q):
    variables = {}
    clauses = []
    choices = {}
    for i in range(n):
        for a, b in itertools.product(range(q), repeat=2):
            group = []
            for g in range(q):
                if g not in (a, b):
                    key = (i, a, b, g)
                    variables[key] = len(variables) + 1
                    group.append(variables[key])
            choices[i, a, b] = group
            clauses.append(group)
            clauses.extend([-u, -v] for u, v in itertools.combinations(group, 2))
    proper_count = 0
    for c in itertools.product(range(q), repeat=n):
        if all(c[i] != c[(i+1) % n] for i in range(n)):
            proper_count += 1
            clauses.append([variables[i, c[(i-1)%n], c[(i+1)%n], c[i]]
                            for i in range(n)])
    # Palette relabeling fixes one output without losing any strategy.
    clauses.append([variables[0, 0, 0, 1]])
    return variables, clauses, proper_count


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('n', type=int)
    ap.add_argument('q', type=int)
    ap.add_argument('--seconds', type=float, default=30)
    ap.add_argument('--solver', default='glucose4')
    args = ap.parse_args()
    v, clauses, count = make_instance(args.n, args.q)
    out = {'n':args.n, 'q':args.q, 'solver':args.solver,
           'variables':len(v), 'clauses':len(clauses), 'proper_colorings':count}
    print(json.dumps(out), flush=True)
    t0 = time.monotonic()
    with Solver(name=args.solver, bootstrap_with=clauses) as s:
        timer = threading.Timer(args.seconds, s.interrupt)
        timer.start()
        try:
            result = s.solve_limited(expect_interrupt=True)
        finally:
            timer.cancel()
        out.update(status={True:'SAT',False:'UNSAT',None:'UNKNOWN'}[result],
                   elapsed=time.monotonic()-t0, stats=s.accum_stats())
        if result:
            model = set(x for x in s.get_model() if x > 0)
            f = {(i,a,b):g for (i,a,b,g), x in v.items() if x in model}
            checked = 0
            failures = []
            for c in itertools.product(range(args.q), repeat=args.n):
                if all(c[i] != c[(i+1)%args.n] for i in range(args.n)):
                    checked += 1
                    if not any(f[i,c[(i-1)%args.n],c[(i+1)%args.n]] == c[i]
                               for i in range(args.n)):
                        failures.append(c)
            assert checked == count
            assert not failures
            out['independent_enumeration'] = {'checked':checked,'failures':0}
            out['strategy'] = [[i,a,b,g] for (i,a,b),g in sorted(f.items())]
    path = Path(__file__).with_name(f'C{args.n}_q{args.q}_{args.solver}.json')
    path.write_text(json.dumps(out, indent=2), encoding='utf-8')
    print(json.dumps({k:x for k,x in out.items() if k!='strategy'}), flush=True)


if __name__ == '__main__':
    main()
