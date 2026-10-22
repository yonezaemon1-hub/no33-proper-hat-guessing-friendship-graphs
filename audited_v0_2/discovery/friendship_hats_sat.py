"""Exact pair-cover encoding for proper hats on F_r = K_1 join r K_2."""
import argparse
import itertools
import json
import sys
import threading
import time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'research_deps'))
from pysat.solvers import Solver


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('petals',type=int)
    ap.add_argument('q',type=int)
    ap.add_argument('--seconds',type=float,default=45)
    ap.add_argument('--solver',default='glucose4')
    ap.add_argument('--cyclic',action='store_true')
    ap.add_argument('--symmetric',action='store_true')
    args=ap.parse_args()
    r,q=args.petals,args.q
    vs={}
    clauses=[]
    for j in range(r):
        for side in range(2):
            for a,y in itertools.permutations(range(q),2):
                group=[]
                for g in range(q):
                    if g not in (a,y):
                        vs[j,side,a,y,g]=len(vs)+1
                        group.append(vs[j,side,a,y,g])
                clauses.append(group)
                clauses.extend([-u,-v] for u,v in itertools.combinations(group,2))
    nxt=len(vs)
    selectors={}
    for a,b in itertools.combinations(range(q),2):
        cover=[]
        for j in range(r):
            nxt+=1
            selectors[j,a,b]=nxt
            cover.append(nxt)
            for x,y in itertools.permutations([k for k in range(q) if k not in (a,b)],2):
                clauses.append([-nxt,vs[j,0,a,y,x],vs[j,1,a,x,y],
                                vs[j,0,b,y,x],vs[j,1,b,x,y]])
        clauses.append(cover)
    if args.cyclic:
        for (j,side,a,y,g),v in vs.items():
            if a==0:continue
            u=vs[j,side,0,(y-a)%q,(g-a)%q]
            clauses.extend([[-v,u],[-u,v]])
    if args.symmetric:
        for (j,side,a,y,g),v in vs.items():
            if side==0:continue
            u=vs[j,0,a,y,g]
            clauses.extend([[-v,u],[-u,v]])
    out={'petals':r,'q':q,'solver':args.solver,'cyclic':args.cyclic,
         'symmetric':args.symmetric,
         'variables':nxt,'clauses':len(clauses)}
    print(json.dumps(out),flush=True)
    t=time.monotonic()
    with Solver(name=args.solver,bootstrap_with=clauses) as s:
        timer=threading.Timer(args.seconds,s.interrupt)
        timer.start()
        try:
            result=s.solve_limited(expect_interrupt=True)
        finally:
            timer.cancel()
        out.update(status={True:'SAT',False:'UNSAT',None:'UNKNOWN'}[result],
                   elapsed=time.monotonic()-t,stats=s.accum_stats())
        if result:
            model={x for x in s.get_model() if x>0}
            f={(j,side,a,y):g for (j,side,a,y,g),v in vs.items() if v in model}
            good=[]
            for j in range(r):
                pairs=[]
                for a,b in itertools.combinations(range(q),2):
                    if all(f[j,0,a,y]==x or f[j,1,a,x]==y or
                           f[j,0,b,y]==x or f[j,1,b,x]==y
                           for x,y in itertools.permutations(
                               [k for k in range(q) if k not in (a,b)],2)):
                        pairs.append([a,b])
                good.append(pairs)
            assert set(itertools.combinations(range(q),2))=={
                tuple(e) for es in good for e in es}
            # Fresh enumeration at fixed actual center colour. The possible
            # colors surviving all petal rules must be exactly the actual one
            # whenever every noncenter guess is incorrect.
            checked=all_outer_wrong=failures=0
            for a in range(q):
                palette=[c for c in range(q) if c!=a]
                patterns=list(itertools.permutations(palette,2))
                for p in itertools.product(patterns,repeat=r):
                    checked+=1
                    if any(f[j,0,a,y]==x or f[j,1,a,x]==y
                           for j,(x,y) in enumerate(p)):
                        continue
                    all_outer_wrong+=1
                    residual=[b for b in range(q)
                        if all(b not in (x,y) and f[j,0,b,y]!=x and f[j,1,b,x]!=y
                               for j,(x,y) in enumerate(p))]
                    failures+=residual!=[a]
            assert not failures
            out['strategy']=[list(k)+[g] for k,g in sorted(f.items())]
            out['good_pairs']=good
            out['independent_enumeration']={'proper_colorings':checked,
                'all_outer_wrong':all_outer_wrong,'failures':failures}
    path=Path(__file__).with_name(f'F{r}_q{q}_{args.solver}'+('_cyclic' if args.cyclic else '')+('_symmetric' if args.symmetric else '')+'.json')
    path.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='strategy'}),flush=True)


if __name__=='__main__':main()
