# No.33 v0.2：砂時計の値6と三花弁の閾値

2026-10-23 / Ryutaro Yonezu, Yonezu Research Lab / 未査読

**主張の中心は「砂時計で厳密に6」「7色に届く最小花弁数が3」。**
対象は \(F_r=K_1\vee(rK_2)\)。
隣接者の帽子が違う proper coloring に対して、各人は隣人だけを見て
自分の色を同時に1回推測する。任意の頂点別戦略を許す。

| 三角形の数 | 最大色数の候補 | 位置付け |
|---:|---:|---|
| 1 | 5 | 既知の完全グラフ定理 |
| 2 | 6 | 本稿の中心となる厳密値 |
| 3以上 | 7 | 最小到達個数が3であることが中心 |

## 最初に読むもの

1. AUDIT_RESPONSE_v0_2.md：受領した外部AI監査への対応と残件
2. PROOF.md：英語の証明原稿
3. REFERENCE_CHECK_v0_2.md：正式引用4本の該当一次本文の照合
4. audit/USER_SUPPLIED_AUDIT_20261023.md：ユーザーから受領した監査本文
5. NOVELTY_AUDIT.md：2026-10-22の検索メモ。状態表記は当時のもの

## 判定

| 項目 | 状態 |
|---|---|
| 一般証明 | 前版への外部AI報告は PASS（条件付き）。v0.2差分の外部確認はPENDING |
| 明示戦略の全探索 | 当方の60＋2,400＋189,000配置、失敗0 |
| 外部報告の自前全探索 | F2：2,400、F3：189,000、失敗0との報告 |
| 引用文献 | 正式引用4本の該当一次箇所を当方で確認。外部監査のREFERENCES=PARTIALとは区別 |
| 新規性 | INCONCLUSIVE。世界初・優先権の主張なし |
| 人間の著者確認・査読 | PENDING / 未査読 |
| Windows実機再現 | 未実施 |
| GitHub / Zenodo | **HOLD** |

当方の「別実装」は同じ助手によるもので、外部独立監査とは異なる。
今回の外部報告はユーザーから提示された本文として保存した。
報告者のプログラム・CP-SAT設定・raw log は同梱されていない。
それらを当方で再実行したとは書かない。

## v0.2で変えた内容

主張の見せ方、引用箇所の具体化、監査の出所・状態表記を整理した。
証明の各補題の論証、下界の表、witness.json、2本のPython検証器、
計算JSON、探索記録は前版を継承する。

単一花弁について必要なのは「次数3以下、したがって10辺以下」。
10辺の達成や最大辺数の厳密最適値を主張しない。
十分多数なら7色に勝てるだけの結果は、既知の複数推測結果と
基本的な補完から21花弁で導けるため、主要な新規性に数えない。

## ローカル検証

Python標準ライブラリのみ。ネット接続・API・課金・追加パッケージ不要。

PowerShellで展開先から実行：

~~~powershell
python .\verify_exhaustive.py
python .\audit_bitmasks.py
~~~

まとめて実行：

~~~powershell
powershell -ExecutionPolicy Bypass -File .\RUN_VERIFY.ps1
~~~

2本は明示構成を検証する。任意戦略に対する上界は PROOF.md の一般証明。
discovery/ 内のUNKNOWNやタイムアウトを不可能性の証拠に使わない。

SHA256SUMS.txt が現行一式のハッシュ（一覧自身を除く）。
ORIGINAL_SHA256SUMS.txt はv0.1原本の履歴資料であり、v0.2の照合には使わない。
公開用PDFは未作成。公開操作も行っていない。

Research inquiries: yonezaemon1+research@gmail.com  
Copyright (c) 2026 Ryutaro Yonezu. All rights reserved.
