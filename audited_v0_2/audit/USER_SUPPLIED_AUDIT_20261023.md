# User-supplied external-AI audit report

Received: 23 October 2026 (JST).
Source: the user's message in this conversation. Inline-code formatting
is normalized; the substantive contents are retained.
No reviewer program, CP-SAT model, raw solver log, or signed audit artifact
was supplied with this text. The memory-creation statement at the end
belongs to the supplied report; it is not a claim that this assistant wrote
that external memory file.

---

No.33の監査を進めています。自前実装で、上界3件（K7を2枚で覆えない／K6は覆える／K8を3枚でも覆えない）と下界の全探索（2,400／189,000配置、失敗0）が通りました。残りは単一花弁の最大辺数の確認、先行研究の確認、数え上げの再確認です。

No.33（友情グラフの proper hat guessing）の主張は、私の検証の範囲では確認できました。ただし人間の査読はなく、新規性も未確定なので、公開は保留（HOLD）です。

## 判定

| 項目          | 判定           |
| ----------- | ------------ |
| PROOF       | PASS（条件付き）   |
| COMPUTATION | PASS         |
| REFERENCES  | PARTIAL      |
| NOVELTY     | INCONCLUSIVE |
| RELEASE     | **HOLD**     |

主張は、F_r = K₁∨(rK₂) の値が r=1 で 5、r=2（砂時計）で 6、r≥3 で 7、というものです。SHA256 は全ファイル一致しました。

## PROOF

- **補題1（ペア被覆の判定条件）**: 論証を読んで確認したうえで、ランダムな葉の規則 600 件（q=4,5、花弁 1〜2 個）で、「ハブの規則が存在する」ことと「ペアグラフ E_i の和が完全グラフになる」ことを総当たりで比べました。不一致は 0 件で、被覆が完全な 189 件と不完全な件の両方が含まれています。
- **補題2（8色は何個の花弁でも不可能）**: 順序対 30 個に対して事象が 4×6=24 個しか覆えません。この計数は正しいです。
- **補題3（7色で 1 花弁の最大次数は 3 以下）**: 等号条件、事象の互いに素性、「像から除かれる」議論を読んで、導出に穴はありません。仮定は循環対称性などに頼っていません。CP-SAT でも、q=7・1 花弁の最大次数は最適値 3 と確認できました。
- 7色で花弁 2 個では最大 20 辺で、21 辺に足りません。CP-SAT では「K₇を花弁 2 個で覆う」が INFEASIBLE、「K₈を花弁 3 個で覆う」も INFEASIBLE でした。
- 同じ CP-SAT で「K₆を花弁 2 個で覆う」は OPTIMAL（実行可能）でした。
- 色数を減らす単調性と、r>3 への拡張（余分な花弁を無視する）も正しいです。
- 1 花弁で最大辺数 10 の直接確認は、100 秒では最適性まで届きませんでした。ただし 10 辺以下は次数 3 以下から従うので、結論には影響しません。

## COMPUTATION

- PROOF.md の表から自前で戦略を組み直し、ハブの規則は見えている葉の配置だけから構成しました。&#x20;
  - F₂・6色: 2,400 配置、失敗 0。
  - F₃・7色: 189,000 配置、失敗 0。
- すべての出力が合法で、色の対応も正しいことを確認しました。
- 負例として、7色で花弁を 2 個に減らすと、ハブの色 {2,6} が区別できなくなり、確かに検出されます。
- 同梱の verify_exhaustive.py と audit_bitmasks.py は実行していません。自前実装で代えました。
- 同梱の SAT 探索ログ（discovery/）は上界の証拠としては使われていません。

## REFERENCES

- Adriaensen らの論文（arXiv:2603.04909）は、原文を取得して確認できました。&#x20;
  - HG_P(K_n)=2n−1 が Theorem 1.1 に書かれています。
  - Table 1 では砂時計が 5〜7 です。
  - friendship と bowtie の語は出ず、windmill は結論で未解決の例として挙げられているだけです。
- He–Ido–Przybocki、Zhai、Kakatelis など他の引用は、今回は一次本文までは確認していません。

## NOVELTY

- 新規性の中心は「砂時計で厳密に 6」と「7 に届く最小の花弁数が 3」です。
- NOVELTY_AUDIT.md は、「花弁 21 個なら 7」は既知の複数推測結果から導けると自己申告しています。この記述は、新規性の主張を絞る方向で妥当です。
- 数値そのものが既出でないかは検索の範囲では見つかりませんでしたが、これは新規性の証明ではありません。優先権の主張は避けてください。

## RELEASE

- 次の一手は、引用文献の一次確認の完了と、原稿の主張を「r=2 で 6、閾値 3」に絞ることです。
- 同梱ファイルでは、「別実装」「内部監査」の記述が同じ助手による作業だと明記されています。このまま保たれており、問題ありません。
- GitHub と Zenodo は HOLD のままにしてください。

メモリに /areas/no33-friendship-hat-guessing.md を新規作成しました。

Sources:

- [Hat guessing with proper colorings (arXiv:2603.04909)](https://arxiv.org/pdf/2603.04909)

