"""Eliminate a universal player's rule exactly, for small proper-hat games."""
import argparse
import itertools
import json
import sys
import threading
import time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'research_deps'))
from pysat.solvers import Solver


def graph(name):
    if name == 'hourglass':
        outer = [(1,2),(3,4)]
    elif name == 'fan':
        outer = [(1,2),(2,3),(3,4)]
    elif name == 'wheel':
        outer = [(1,2),(2,3),(3,4),(4,1)]
    elif name == 'diamond':
        outer = [(1,2),(2,3)]
    else:
        raise ValueError(name)
    n = max(max(e) for e in outer)+1
    edges = [(0,i) for i in range(1,n)] + outer
    neighbors = {i: sorted(j for a,b in edges for j in
                           ([b] if a==i else [a] if b==i else [])) for i in range(n)}
    return n, edges, outer, neighbors


def instance(name,q):
    n,edges,outer,nb = graph(name)
    vs = {}
    clauses = []
    for i in range(1,n):
        for p in itertools.product(range(q), repeat=len(nb[i])):
            # Every neighbor of outer i is adjacent to universal 0.
            col = dict(zip(nb[i],p))
            if any(col[a]==col[b] for a,b in edges if a in col and b in col):
                continue
            group = []
            for g in range(q):
                if g not in p:
                    vs[i,p,g] = len(vs)+1
                    group.append(vs[i,p,g])
            clauses.append(group)
            clauses.extend([-a,-b] for a,b in itertools.combinations(group,2))
    pair_constraints = 0
    for a,b in itertools.combinations(range(q),2):
        palette = [x for x in range(q) if x not in (a,b)]
        for p in itertools.product(palette, repeat=n-1):
            c=[a]+list(p)
            if any(c[u]==c[v] for u,v in outer):
                continue
            cl=[]
            for center in (a,b):
                c[0]=center
                for i in range(1,n):
                    cl.append(vs[i,tuple(c[j] for j in nb[i]),c[i]])
            clauses.append(sorted(set(cl)))
            pair_constraints+=1
    return n,edges,nb,vs,clauses,pair_constraints


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('graph',choices=['hourglass','fan','wheel','diamond'])
    ap.add_argument('q',type=int)
    ap.add_argument('--seconds',type=float,default=45)
    ap.add_argument('--solver',default='glucose4')
    args=ap.parse_args()
    n,edges,nb,vs,clauses,pc=instance(args.graph,args.q)
    out={'graph':args.graph,'n':n,'q':args.q,'solver':args.solver,
         'variables':len(vs),'clauses':len(clauses),'pair_constraints':pc}
    print(json.dumps(out),flush=True)
    t=time.monotonic()
    with Solver(name=args.solver,bootstrap_with=clauses) as s:
        timer=threading.Timer(args.seconds,s.interrupt)
        timer.start()
        try:
            r=s.solve_limited(expect_interrupt=True)
        finally:
            timer.cancel()
        out.update(status={True:'SAT',False:'UNSAT',None:'UNKNOWN'}[r],
                   elapsed=time.monotonic()-t,stats=s.accum_stats())
        if r:
            model=set(x for x in s.get_model() if x>0)
            f={(i,p):g for (i,p,g),x in vs.items() if x in model}
            center={}
            for p in itertools.product(range(args.q),repeat=n-1):
                residual=[]
                for a in range(args.q):
                    c=[a]+list(p)
                    if any(c[u]==c[v] for u,v in edges):
                        continue
                    if not any(f[i,tuple(c[j] for j in nb[i])]==c[i] for i in range(1,n)):
                        residual.append(a)
                assert len(residual)<=1
                legal=[x for x in range(args.q) if x not in p]
                center[p]=residual[0] if residual else (legal[0] if legal else 0)
            checked=failures=0
            for c in itertools.product(range(args.q),repeat=n):
                if any(c[u]==c[v] for u,v in edges):
                    continue
                checked+=1
                wins=center[c[1:]]==c[0] or any(
                    f[i,tuple(c[j] for j in nb[i])]==c[i] for i in range(1,n))
                failures+=not wins
            assert not failures
            out['independent_enumeration']={'checked':checked,'failures':failures}
            out['outer_strategy']=[[i,list(p),g] for (i,p),g in sorted(f.items())]
            out['center_strategy']=[[list(p),g] for p,g in sorted(center.items())]
    Path(__file__).with_name(f'{args.graph}_q{args.q}_{args.solver}.json').write_text(
        json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if not k.endswith('strategy')}),flush=True)


if __name__=='__main__':
    main()
