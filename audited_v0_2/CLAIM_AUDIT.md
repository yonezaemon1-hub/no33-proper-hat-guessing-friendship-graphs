# Internal claim audit, with v0.2 status update

Status update, 23 October 2026: the user supplied an external-AI report for
the preceding version with PROOF conditional PASS and COMPUTATION PASS.
Its text is in audit/USER_SUPPLIED_AUDIT_20261023.md; no raw reviewer
program or solver logs were supplied. This does not turn the internal
checks below into independent checks. References [1]–[4] were checked in
their relevant primary passages by the originating assistant; see
REFERENCE_CHECK_v0_2.md. External review of v0.2 and human review remain
pending. NOVELTY=INCONCLUSIVE; RELEASE=HOLD.

Date: 2026-10-22. Reviewer: the same ChatGPT assistant that developed this
candidate, using separate calculations and implementations. This is not an
external independent-AI audit, human peer review, or formal proof checking.

| Claim | Evidence in this bundle | Current status |
|---|---|---|
| Correct model | Explicit graph edges and permissible observations in PROOF.md | INTERNAL PASS |
| Legal-output normalization | Replacing an always-incorrect output cannot remove a correct guess | INTERNAL PASS |
| Exact pair-cover criterion for arbitrary leaf functions | Common-view two-color adversary; surviving-color completion | INTERNAL PASS |
| Eight-color exclusion for any number of petals | 30 ordered pairs versus at most 24 covered pairs, followed by Lemma 1 | INTERNAL PASS |
| Seven-color single-petal maximum degree at most 3 | Equality/disjointness argument, omitted-image argument, forced double correctness | INTERNAL PASS |
| Seven-color exclusion on two petals | At most 10+10 edges versus 21 | INTERNAL PASS |
| Six-color lower bound | Explicit 10-entry cyclic tables; handwritten local-cover checks; full enumeration | PASS in checked computations |
| Seven-color lower bound on three petals | Six-entry base table and three scalings; local tournament check; full enumeration | PASS in checked computations |
| All r>=3 lower bound | Ignore additional petals at the hub; winning induced F3 strategy persists | INTERNAL PASS |
| Five-color triangle value | Established theorem; 60-coloring reproduction and elementary upper count | PASS; known result |
| Worldwide novelty | Bounded comparison only | INCONCLUSIVE |
| Windows 10 / Python 3.12.10 execution | Portable standard-library scripts prepared; not run on user's machine | NOT TESTED |
| Publication | User explicitly requires GitHub and Zenodo to remain HOLD | HOLD |

## Computation checks performed

1. Actual hub lookup construction followed by exhaustive checking of 60,
   2,400, and 189,000 proper full colorings: zero failures.
2. Separate literal-table implementation using intersection of surviving
   hub-color bit masks: 20, 900, and 74,088 outer views; zero ambiguities.
3. A legal change to the seven-color base table produces an explicit
   two-hub-color counterexample, detected by the audit.
4. Removing the third seven-color petal produces a two-color ambiguity.
   This negative control is about this construction only; the proof of
   impossibility for *every* two-petal strategy is Lemmas 1 and 3.

## Main universality checks

- Cyclic and left/right-symmetric rules occur only in lower constructions.
  Upper arguments allow arbitrary vertex-specific leaf functions.
- The hub lookup is built from its visible leaf vector before testing
  actual hub colors. It never receives its own color.
- Proper coloring is enforced within each triangle and across the hub;
  leaves in different petals may share colors.
- The parameter counts palette colors; it does not require every color
  to appear in each assignment.
- Search UNKNOWN is not UNSAT, and neither is used to establish an upper
  bound. Exact upper arguments are combinatorial.
- Verification in the two bundled implementations still shares the
  mathematical idea and authoring assistant. The separately supplied
  external-AI report and its evidence limits are recorded above; human
  review and external review of the v0.2 changes remain pending.
