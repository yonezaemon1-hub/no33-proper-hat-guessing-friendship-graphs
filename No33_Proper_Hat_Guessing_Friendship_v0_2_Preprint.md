---
title: "Proper Hat Guessing on Friendship Graphs: The Hourglass Value and the Three-Petal Threshold"
author: "Ryutaro Yonezu (Yonezu Research Lab)"
date: "23 October 2026 | v0.2 public preprint"
fontsize: 10pt
papersize: a4
geometry: margin=22mm
colorlinks: true
linkcolor: black
urlcolor: blue
header-includes:
  - \usepackage{amsmath,amssymb,booktabs,longtable,microtype}
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhf{}
  - \fancyfoot[C]{\thepage}
  - \renewcommand{\headrulewidth}{0pt}
---

**Unrefereed, AI-assisted preprint.** The mathematical content below follows
`PROOF.md` in the frozen v0.2 audit archive. Publication was authorized by
the author on 23 October 2026; that authorization is not human peer review.
A user-supplied external-AI differential report records PROOF PASS
(conditional) and COMPUTATION PASS. REFERENCES remain PARTIAL and
historical NOVELTY remains INCONCLUSIVE. No priority claim, human
refereeing, or proof-assistant certification is made. The historical HOLD
notices in the unchanged audit archive are retained as audit history.

## 1. Model and exact-value candidate

Let

\[
F_r=K_1\vee(rK_2),\qquad r\geq1.
\]

The hub is \(v\), and the leaves of petal \(i\) are \(u_i,w_i\).
Its edges are \(vu_i,vw_i,u_iw_i\), for \(1\leq i\leq r\), with no others.
Thus \(F_r\) consists of \(r\) triangles with one common vertex.
It is also the triangular windmill \(W_{3,r}\); \(F_2\) is the hourglass or
bowtie graph. These names do not denote two triangles sharing an edge.

The palette is \(Q=\{0,\ldots,q-1\}\). An adversary chooses a proper vertex
coloring: adjacent vertices have distinct colors. Each player sees its own
open neighborhood, makes one simultaneous deterministic guess for its own
color, and the team wins if at least one guess is right. Different vertices
may have different functions and may distinguish their neighbors. No
anonymous, affine, cyclic, or symmetry restriction is imposed on the model.

Write \(\operatorname{HG}_P(G)\) for the largest winning palette size.

**Main result candidate.** The hourglass has
\(\operatorname{HG}_P(F_2)=6\), and three is the smallest positive number
of petals for which seven colors are winning. Together with the known
triangle value, the uniform upper bound, and the extension argument below,
this gives, for every integer \(r\geq1\),

\[
\operatorname{HG}_P(F_r)=
\begin{cases}
5,&r=1,\\
6,&r=2,\\
7,&r\geq3.
\end{cases}
\]

The first case is already the complete-graph theorem of Adriaensen et al.
[1]. In [1, v4, Table 1], the hourglass is listed with bounds 5 and 7.
The possible contribution of this note is its specific evaluation at
\(r=2\) and the sharp three-petal saturation statement for this established
model. It does not claim invention of the game, of friendship graphs, or
of a general observation-completion method.

## 2. Local functions and a pair-cover criterion

Write \(L_i(a,y)\) for \(u_i\)'s guess when the hub has color \(a\) and
\(w_i\) has color \(y\), and \(R_i(a,x)\) for \(w_i\)'s corresponding rule.
For \(q\geq3\), we may assume

\[
L_i(a,y)\notin\{a,y\},\qquad R_i(a,x)\notin\{a,x\}
\quad(a\ne y,\ a\ne x).
\]

An output equal to a visible color is never correct under a proper
coloring, so replacing it by any legal color cannot destroy a win.
Every distinct pair \((a,y)\) is an attainable leaf view in \(F_r\).

For fixed leaf rules, define a graph \(E_i\) on the palette \(Q\). Its
edge \(\{a,b\}\), with \(a\ne b\), is present exactly when, for every
ordered pair of distinct colors \(x,y\in Q\setminus\{a,b\}\),

\[
L_i(a,y)=x\ \lor\ R_i(a,x)=y\ \lor\
L_i(b,y)=x\ \lor\ R_i(b,x)=y. \tag{1}
\]

**Lemma 1 (pair-cover criterion).** The fixed leaf rules admit a winning
hub rule if and only if \(E_1\cup\cdots\cup E_r=K_q\).

*Proof.* If a pair \(\{a,b\}\) is absent from every \(E_i\), choose in
each petal distinct colors \(x_i,y_i\notin\{a,b\}\) for which all four
equalities in (1) fail. With this common observed leaf vector, both hub
colors \(a,b\) give proper colorings and make all leaves wrong. The hub
sees the same vector in both colorings, so it must be wrong in at least
one. Thus its rule cannot be winning.

Conversely, for an observed leaf vector \(p=((x_i,y_i))_{i=1}^r\), put

\[
S(p)=\{a\in Q:\ a\notin\{x_i,y_i\},\
L_i(a,y_i)\ne x_i,\ R_i(a,x_i)\ne y_i\text{ for every }i\}.
\]

If two different colors \(a,b\) belonged to \(S(p)\), the pair would be
absent from every \(E_i\), contrary to the assumed cover. Hence
\(|S(p)|\leq1\). The hub guesses its sole element when one exists, and
guesses arbitrarily otherwise. Whenever all leaves are wrong, the actual
hub color belongs to \(S(p)\), so the hub is right. Its rule depends only
on the leaf colors it sees, not on its own color. This is a simultaneous
local strategy and requires no communication during play. \(\square\)

This is a specialization of the familiar idea of completing the rule at
a common vertex after fixing rules on independent pieces; related
frameworks appear in [2, Lemma 4.4] and [3, Lemma 3.3]. No claim that this
general idea is new is intended.

## 3. Eight colors are impossible for every number of petals

**Lemma 2.** For all \(r\geq1\), \(\operatorname{HG}_P(F_r)\leq7\).

*Proof.* At \(q=8\), fix any two distinct prospective hub colors \(a,b\).
There are \(6\cdot5=30\) ordered distinct leaf-color pairs in
\(T=Q\setminus\{a,b\}\). For one petal, each of the four equalities in
(1) holds for at most six such pairs: for example, fixing \(y\) determines
at most one \(x=L_i(a,y)\). The four events therefore cover at most
\(4\cdot6=24<30\) pairs. Thus \(\{a,b\}\) is absent from every \(E_i\).
Lemma 1 excludes a winning strategy, regardless of \(r\).

A winning strategy on a larger palette would restrict to one on eight
colors: retain guesses inside the restricted palette and replace other
outputs arbitrarily. Correct guesses on restricted colorings are
preserved. Therefore no larger palette is winning either. \(\square\)

## 4. Seven-color rigidity excludes the hourglass

The next argument treats arbitrary legal functions \(L,R\) for a single
petal. In particular it does not assume the symmetric cyclic form of the
constructions below.

**Lemma 3.** At \(q=7\), the pair graph \(E\) of one petal has maximum
degree at most 3, and hence at most 10 edges.

*Proof.* Suppose \(\{a,b\}\in E\), and let \(T=Q\setminus\{a,b\}\).
There are 20 ordered pairs of distinct elements of \(T\). The four
correctness events in (1) each have size at most five. Since their union
covers all 20 pairs, each event has size exactly five, and the four events
are pairwise disjoint.

In particular, \(L(a,y)\) belongs to \(T\setminus\{y\}\) for every
\(y\in T\): otherwise the event \(L(a,y)=x\) would have fewer than five
pairs. Together with legality at \(y=b\), this shows that
\(L(a,y)\ne b\) for every \(y\ne a\). Likewise
\(R(a,x)\ne b\) for every \(x\ne a\). Thus each neighbor \(b\) of
\(a\) in \(E\) is omitted from the entire images of both functions at
hub color \(a\).

If \(a\) had four distinct neighbors forming a set \(B\), all outputs
of \(L(a,\cdot)\) and \(R(a,\cdot)\) would lie in the two-element set
\(U=Q\setminus(\{a\}\cup B)=\{s,t\}\). Legality forces
\(L(a,t)=s\) and \(R(a,s)=t\). Choose any \(b\in B\). Then
\((x,y)=(s,t)\) is one of the 20 pairs for \(\{a,b\}\), and both
events \(L(a,y)=x\) and \(R(a,x)=y\) hold. This contradicts their
disjointness. Consequently the maximum degree is at most 3, giving
\(|E|\leq\lfloor7\cdot3/2\rfloor=10\). \(\square\)

**Corollary 4.** \(\operatorname{HG}_P(F_2)\leq6\).

*Proof.* Two seven-color petal graphs cover at most 20 edges in total,
whereas \(K_7\) has 21 edges. Apply Lemma 1, then palette restriction
to exclude all larger palettes as well. \(\square\)

The equality condition in Lemma 3 is essential. Merely bounding each
event by five, without deriving disjointness, does not prove this result.
The number 10 is an upper bound on the number of edges, not an asserted
attainable optimum. No construction attaining 10 edges, or optimization
certificate for that objective, is needed for Corollary 4.

## 5. An explicit six-color strategy on two petals

Use arithmetic modulo 6. Define functions on nonzero differences by

| \(d\) | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| \(A(d)\) | 4 | 3 | 1 | 3 | 3 |
| \(B(d)\) | 4 | 5 | 4 | 5 | 1 |

Both leaves in the first petal guess
\(f_A(a,y)=a+A(y-a)\pmod6\), and both leaves in the second use
\(f_B(a,y)=a+B(y-a)\pmod6\). All outputs are legal.

The \(A\)-petal covers every hub pair whose difference is \(\pm1\) or
\(\pm2\); the \(B\)-petal covers every pair of difference 3. Translation
invariance reduces verification to hub pairs \(\{0,1\}\),
\(\{0,2\}\), and \(\{0,3\}\), respectively.

For a symmetric leaf rule, an unordered leaf-color pair \(\{x,y\}\) is
covered at hub color \(a\) if \(f(a,y)=x\) or \(f(a,x)=y\). The following
lists of covered unordered pairs verify all three cases directly. A pair
such as 23 denotes \(\{2,3\}\), not the integer twenty-three.

| Hub pair; rule | Remaining leaf palette | Covered at hub 0 | Covered at the other hub color |
|---|---|---|---|
| \(\{0,1\}; A\) | \(\{2,3,4,5\}\) | 23, 34, 35 | 25, 34, 24, 45 |
| \(\{0,2\}; A\) | \(\{1,3,4,5\}\) | 14, 13, 34, 35 | 15, 45, 35 |
| \(\{0,3\}; B\) | \(\{1,2,4,5\}\) | 14, 25, 45, 15 | 12, 24, 14, 25 |

In each row the union is all six pairs of the remaining four colors.
The pair graphs cover \(K_6\), so Lemma 1 supplies the hub rule. This
proves the lower bound 6, completing the exact hourglass value with
Corollary 4.

## 6. An explicit seven-color strategy on three petals

Use arithmetic modulo 7, and set

| \(t\) | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|
| \(h(t)\) | 3 | 5 | 2 | 5 | 3 | 2 |

Index the three petals by \(d\in\{1,2,3\}\). Both leaves of petal \(d\)
use

\[
f_d(a,y)=a+d\,h\bigl(d^{-1}(y-a)\bigr)\pmod7. \tag{2}
\]

Here \(d^{-1}\) is the inverse modulo 7; the argument of \(h\) is never
zero in a proper local view. The values of \(h\) differ from both zero
and their arguments, so (2) is legal.

We show that petal \(d\) covers all hub pairs of difference \(\pm d\).
Translation and scaling reduce this to \(d=1\), hub pair \(\{0,1\}\).
The remaining colors are \(T=\{2,3,4,5,6\}\). For \(y\in T\), the two
guesses at hypothetical hub colors 0 and 1 are:

| \(y\) | \(f_1(0,y)\) | \(f_1(1,y)\) |
|---:|---:|---:|
| 2 | 5 | 4 |
| 3 | 2 | 6 |
| 4 | 5 | 3 |
| 5 | 3 | 6 |
| 6 | 2 | 4 |

The ten directed pairs from a row label to its two outputs contain
exactly one orientation of each unordered pair of distinct elements of
\(T\). Thus, for every ordered distinct \((x,y)\in T^2\), either
\(x\in\{f_1(0,y),f_1(1,y)\}\), or
\(y\in\{f_1(0,x),f_1(1,x)\}\). This is precisely (1).

The three differences \(\pm1,\pm2,\pm3\) exhaust the six nonzero
differences modulo 7, so the three petal graphs cover \(K_7\).
Lemma 1 gives the hub rule, proving a winning seven-color strategy.
For \(r>3\), retain this strategy on three selected petals: the hub
ignores its additional neighbors and all added leaves may guess
arbitrarily. Every proper coloring restricts to a proper coloring on
the selected \(F_3\). Lemma 2 now proves the exact value 7 for every
\(r\geq3\).

## 7. The one-petal case and computational evidence

Since \(F_1=K_3\), [1, Theorem 1.1] gives the already known value 5.
It also follows from a simple upper count and a finite construction.
At \(q=6\), there are \(6\cdot5\cdot4=120\) proper triangle colorings;
each player can be right in at most \(6\cdot5=30\) of them, so three
players cannot cover all colorings. A five-color construction is
included in `witness.json` for reproducibility.

The finite lower-bound checks enumerate, respectively,

\[
5(4\cdot3)=60,\quad
6(5\cdot4)^2=2400,\quad
7(6\cdot5)^3=189000
\]

proper colorings. `verify_exhaustive.py` constructs an actual hub lookup
table before checking all proper colorings. `audit_bitmasks.py` separately
checks intersections of per-petal surviving-hub bit masks over all outer
views. Neither requires a SAT solver, network access, paid API, or extra
Python packages. They verify explicit constructions, not a search over
all possible strategies. The universal upper bounds are the mathematical
arguments in Sections 3–4. Finite computation is unnecessary for their
universal quantifiers.

Exploratory SAT searches helped find the tables. Several unrestricted
searches ended UNKNOWN and provide no nonexistence evidence. Cyclic and
leaf-symmetric restrictions were used only to simplify lower-bound
constructions. The delivered proofs do not rely on SAT status, floating
point calculations, or timeouts.

## 8. Prior-art and claim limits

The proper-coloring model, complete-graph value, and the initial hourglass
bounds are due to [1]. Ordinary windmill hat guessing is treated in [2],
and a proper-coloring coverability framework for a different family of
book graphs is developed in [3]. A recent general upper bound is [4].
These are essential comparisons, not evidence of a newly invented model.

The portions of references [1]–[4] cited here were checked in their primary
texts by the originating assistant on 23 October 2026. The exact locations
and the distinction between ordinary windmills and proper books are recorded
in `REFERENCE_CHECK_v0_2.md`. This is a check of the relevant passages,
not a line-by-line audit of all proofs in all four papers.

Eventual attainment of seven by itself is a weaker contribution than the
sharp threshold. The multiple-guess remark in [1, Section 7, following
Problem 7.1] supplies a five-color proper strategy on an edge with two
guesses at each endpoint. Alternatively, this fact follows directly by
letting both endpoints guess the observed color plus 1 and plus 2 modulo 5.
Assign one petal to each of the 21 unordered pairs of prospective hub
colors and use the first or second guess according to that hub color.
On the other five colors this petal excludes simultaneous failure for
both hub candidates. Lemma 1 then gives a seven-color strategy on 21
petals. This is our elementary deduction from a known result, not a theorem
about friendship graphs claimed to appear in [1]. Details are in
`REFERENCE_CHECK_v0_2.md`. The claimed contribution remains the exact
hourglass value and the least-petal threshold three.

Targeted searches through 22 October 2026 did not locate this specific
evaluation. That is a bounded search result, not proof of worldwide novelty.
The user-supplied external-AI report and its evidence limits are preserved
in `audit/USER_SUPPLIED_AUDIT_20261023.md` and `AUDIT_RESPONSE_v0_2.md`.
It does not supply the reviewer's CP-SAT program or raw solver logs, and we
do not claim to have rerun those computations. No priority, human refereeing,
or proof-assistant verification claim is made. The author authorized public preprint release on 23 October 2026.
The frozen audit archive retains its original historical HOLD statements.
See `PRIOR_ART.md`, `READ_FIRST.md`, and the accompanying publication-status
addendum for the distinction between that history and the present release.

## References

1. S. Adriaensen, P. Bentley, A. Bishnoi, W. Cames van Batenburg,
   M. Kreiger, L. van der Kuil, S. Mandal, A. Ramachandran, and J. Tuite.
   *Hat guessing with proper colorings*. arXiv:2603.04909v4,
   24 August 2026. https://arxiv.org/html/2603.04909v4
2. X. He, Y. Ido, and B. Przybocki. *Hat Guessing on Books and Windmills*.
   Electronic Journal of Combinatorics 29(1) (2022), Paper 1.12.
   Preprint: https://arxiv.org/html/2010.13249v1
   Published version: https://www.combinatorics.org/ojs/index.php/eljc/article/view/v29i1p12
3. Y. Zhai. *Proper Hat-Guessing on Two-Spine Book Graphs*.
   arXiv:2607.25274v3, 18 August 2026.
   https://arxiv.org/html/2607.25274v3
4. I. Kakatelis. *An upper bound on the proper hat guessing number of graphs*.
   arXiv:2610.04124v2, 6 October 2026.
   https://arxiv.org/pdf/2610.04124v2

Research inquiries: yonezaemon1+research@gmail.com  
Copyright (c) 2026 Ryutaro Yonezu. All rights reserved.
