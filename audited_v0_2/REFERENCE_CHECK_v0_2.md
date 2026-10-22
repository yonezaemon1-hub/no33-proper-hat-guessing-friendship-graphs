# No.33 v0.2: primary-reference check

Checked: 23 October 2026 (JST). Checker: the same ChatGPT assistant that
prepared the candidate. Scope: primary passages relevant to the four
references in PROOF.md. This is not an independent bibliography audit,
a complete proof audit of those papers, or a certification of priority.

## Evidence map

| Reference | Primary text inspected | Specific relation to this note |
|---|---|---|
| [1] Adriaensen et al., [2603.04909v4](https://arxiv.org/html/2603.04909v4), 24 August 2026 | Introduction/model; Theorem 1.1; Lemma 1.2; Table 1; Section 7 after Problem 7.1 | The proper model and clique values are established; Table 1 gives the hourglass interval 5–7. The multiple-guess remark supports the premise used below. |
| [2] He–Ido–Przybocki, [2010.13249v1](https://arxiv.org/html/2010.13249v1), 25 October 2020; published EJC 29(1), P1.12 (2022) | Introduction/model; Theorem 1.4; Definition 4.1; Lemma 4.4 and its proof; proof of Theorem 1.4 | Same windmill family in the ordinary game. The completion/packing architecture predates this note; the proper values are not stated there. Numbered references here refer to the inspected preprint version. |
| [3] Zhai, [2607.25274v3](https://arxiv.org/html/2607.25274v3), 18 August 2026 | Sections 1.1 and 2.1; Definition 3.1; Lemmas 3.2–3.5 | The proper book model and target/guarding criterion are established. Its independent pages differ from the adjacent leaf pairs of the present friendship graph. |
| [4] Kakatelis, [2610.04124v2](https://arxiv.org/pdf/2610.04124v2), 6 October 2026 | Introduction and Theorem 1.1 on PDF page 2 | General order/maximum-degree bound; numerical substitution below does not settle the small cases. |

The formulas and graph comparisons below are calculations in this note.
None is attributed as an explicit friendship-graph theorem of [1]–[4].

## Ordinary windmills versus the proper model

Definition 4.1 of [2] identifies \(W_{k,n}\) as \(n\) copies of \(K_k\)
sharing one vertex. Hence its \(W_{3,r}\) is our \(F_r\).
Theorem 1.4 gives \(\mathrm{HG}(W_{k,n})=2k-2\) for
\(n\ge\log_2(2k-2)\). At \(k=3\), this yields the ordinary value 4
for every \(r\ge2\).

That game admits every coloring. Our game admits only proper colorings.
An impossibility proof for the larger set of assignments cannot simply
be transferred to the restricted set. The ordinary value therefore does
not imply the proper values 6 and 7. Lemma 4.4 nevertheless supplies a
clear precedent for completing the hub after fixing the blade rules.

## Proper books versus friendship graphs

In [3], \(B_{k,n}=K_k\vee\overline K_n\).
The \(k\) spine vertices are mutually adjacent; the \(n\) pages are
independent. Lemma 3.3 characterizes when fixed page functions can be
completed by the spines, using coverability of the remaining target tuples.

In \(F_r=K_1\vee(rK_2)\), each leaf sees both the hub and its adjacent
partner. There are edges among the peripheral vertices.
The definitions do not identify these two graph families.
The lemma is a methodological precedent, not the specific pair-graph
degree bound or the exact hourglass evaluation.

## General bounds do not give the two small exact values

For \(F_r\), \(n=2r+1,\chi=3,\Delta=2r\).
Lemma 1.2 of [1] and Theorem 1.1 of [4] respectively give

\[
\mathrm{HG}_P(G)\le n+\chi(G)-1,\qquad
\mathrm{HG}_P(G)\le \frac32+\Delta+
\frac{\sqrt{2n^2+2n\Delta-10n+9}}2.
\]

| Graph | First upper bound | Second upper bound | Candidate value |
|---|---:|---:|---:|
| \(F_2\): \(n=5,\Delta=4\) | 7 | 9 | 6 |
| \(F_3\): \(n=7,\Delta=6\) | 9 | 13 | 7 |

These substitutions do not settle either target value. This comparison
does not claim that every theorem in the literature has been excluded.

## A direct 21-petal consequence and why the threshold matters

The multiple-guess premise from [1, Section 7] has a short independent
verification. On a proper five-color edge, label colors modulo 5 and
let each endpoint guess the observed color plus 1 and plus 2. For
distinct actual colors \(x,y\), the difference \(x-y\) is one of
\(1,2,-1,-2\), so one of the four guesses is correct.

Now use a seven-color palette \(Q\).
For each unordered pair \(\{a,b\}\subset Q\), dedicate one petal.
Identify \(T=Q\setminus\{a,b\}\) with \(\mathbb Z/5\mathbb Z\) in any
fixed order. At hypothetical hub color \(a\), each leaf uses the
plus-1 guess on \(T\); at hypothetical hub color \(b\), it uses plus-2.
On all other legal views define any legal guess.

For every distinct \(x,y\in T\), at least one leaf is right for at least
one of the two hub colors. Thus this petal's pair graph contains
\(\{a,b\}\). The 21 dedicated petals cover \(K_7\), and Lemma 1
completes the hub. All these local guesses avoid the observed partner
and the hub color. This establishes
\(\mathrm{HG}_P(F_{21})\ge7\).
Together with the elementary eight-color obstruction, it gives eventual
value 7 without determining the least number of petals.

This deduction is ours; the source does not state it as a friendship-graph
theorem. Consequently the contribution to retain is \(F_2=6\) and the
sharp threshold 3, rather than eventual stabilization alone.

## Review boundaries

- Relevant primary passages in the four formal references: checked here.
- Other leads in the earlier novelty memo: retain that memo's stated scope;
  this check does not promote every lead to a fully reviewed paper.
- The supplied external-AI report independently read only [1]; its
  REFERENCES=PARTIAL assessment remains part of the audit history.
- Exact optimum of the single-petal edge count: not claimed. The proof
  needs only \(\Delta(E)\le3\), hence \(|E|\le10\).
- The bounded novelty search has cutoff 22 October 2026; today's work
  rechecks primary passages and does not assert an exhaustive new search.
- Human refereeing, reviewer program/log verification, and external review
  of v0.2: not completed. NOVELTY=INCONCLUSIVE; RELEASE=HOLD.

