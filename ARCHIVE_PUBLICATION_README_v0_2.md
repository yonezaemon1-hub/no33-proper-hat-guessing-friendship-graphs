# No.33 — Proper Hat Guessing on Friendship Graphs

**Proper Hat Guessing on Friendship Graphs: The Hourglass Value and the Three-Petal Threshold**  
Ryutaro Yonezu · Yonezu Research Lab · v0.2 · 23 October 2026

Unrefereed, AI-assisted preprint. The author authorized public dissemination on 23 October 2026. PROOF: conditional PASS in the received external-AI report. COMPUTATION: PASS in the checked finite constructions. REFERENCES: PARTIAL. Historical NOVELTY: INCONCLUSIVE. No human peer review, formal proof-assistant certification, priority, or first-discovery claim.

## Result and scope

For the established proper-coloring, one-guess-per-vertex model on `F_r = K_1 ∨ (r K_2)`, the manuscript gives values 5 for one petal, 6 for two petals, and 7 for every number of petals at least three. The five-color triangle value is already known. The claimed finite contribution is the exact hourglass value six and the sharp three-petal threshold for seven colors. Arbitrary vertex-specific local strategies are allowed in the upper bounds; cyclic symmetry is used only to present the explicit lower constructions.

## Files

- [Five-page public preprint](No33_Proper_Hat_Guessing_Friendship_v0_2_Preprint.pdf).
- [Typesetting source](No33_Proper_Hat_Guessing_Friendship_v0_2_Preprint.md).
- [Publication evidence bundle](No33_Friendship_Hat_Guessing_v0_2_Publication_Evidence.zip).
- [Original frozen audit ZIP](No33_Audit_v0_2.zip), SHA-256 `8610cac5537fa17592342654f7df384fa139e6702b5568bb914e25d9a9b55139`.
- [Publication status and provenance](PUBLICATION_STATUS_20261023.md).
- [Received differential-audit record](EXTERNAL_DIFFERENTIAL_AUDIT_RECEIPT_20261023.md).
- `audited_v0_2/` preserves all 41 original audit files, including proofs, references, code, witnesses, solver-discovery history, and the original manifest.
- `PUBLICATION_SHA256SUMS.txt` covers the packaged publication files. The external publication ZIP itself is excluded from its own internal manifest.

## Offline reproduction

From `audited_v0_2/`, Python 3.12 and the standard library suffice:

```text
python verify_exhaustive.py
python audit_bitmasks.py
```

A fresh publication check enumerated 60, 2,400, and 189,000 proper colorings with zero failures. The bitmask checks had zero ambiguous views across 20, 900, and 74,088 outer views, and both negative controls produced counterexamples. These checks verify the displayed constructions. The universal upper bounds are the mathematical arguments in the manuscript, not exhaustive searches over all strategies.

## Historical labels and limitations

Original HOLD, pending-review, and PDF-not-yet-created statements inside the unchanged audit files describe their preparation stage. The separately dated publication status records the later author authorization and received differential audit. Authorization does not attest that a human completed the outstanding reference checks. The reviewer’s raw program and solver logs were not supplied. No Windows run on the author's machine is claimed.

The public PDF changes publication-status wording and typesetting only; the mathematical body follows the frozen `PROOF.md`. The original archive is not repacked or overwritten.

## Rights and contact

© 2026 Ryutaro Yonezu / Yonezu Research Lab. **All rights reserved. No general reuse license is granted.**

Research inquiries: yonezaemon1+research@gmail.com

GitHub: https://github.com/yonezaemon1-hub/no33-proper-hat-guessing-friendship-graphs
