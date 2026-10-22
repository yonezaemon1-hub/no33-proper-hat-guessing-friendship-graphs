# No.33 新規性検索・比較監査

履歴注記（2026-10-23）：以下は2026-10-22の検索メモで、監査状態も当時のもの。
今回受領した外部AI報告とv0.2の現状は READ_FIRST.md / AUDIT_RESPONSE_v0_2.md を参照。

調査日：2026年10月22日  
対象：Proper Hat Guessing on Friendship Graphs  
判定：**同一先行結果は今回の調査では未発見。新規性は INCONCLUSIVE。候補は維持。**

## 1. 今回残す主張

中心1頂点を共有する \(r\) 個の三角形を
\(F_r=K_1\vee(rK_2)\) とする。頂点ごとに任意の決定的な1回推測を許し、相手の配置を proper coloring に制限する標準モデルで、候補定理は

\[
\mathrm{HG}_P(F_r)=
\begin{cases}
5,&r=1,\\
6,&r=2,\\
7,&r\ge3.
\end{cases}
\]

**新規性候補の中心は \(\mathrm{HG}_P(F_2)=6\) と、7に到達する三角形数の最小値が3であること。**

\(F_2\) は hourglass / bowtie / butterfly。三角形が共有するのは1頂点であり、1辺を共有する book graph とは異なる。windmill の添字順には文献差があるため、名称だけでなく上のグラフ式で比較した。

## 2. 主張の切り分け

| 部分 | 今回の分類 | 原稿での扱い |
|---|---|---|
| proper-coloring 制約のゲーム、任意の局所戦略 | 既存モデル | モデルの導入論文を引用する |
| \(r=1\) の値5 | 既知の clique 結果 | 新規結果に数えない |
| 周辺頂点の戦略を固定し、中心の推測を補完する構成 | 既存研究に根がある方法 | completion / coverability の系譜を明記する |
| 複数の中心色に共通する周辺の失敗を作る上界の構図 | 既存の計数的手法と近い | 方法自体の新規性を主張しない |
| 「十分多数なら7に到達する」だけ | 既知の複数推測結果から容易に導ける部分がある | 下記の21個構成を踏まえ、主結果の売りにしない |
| 2個で厳密に6、7到達の最小個数が3 | 同一結果を未発見 | 残る候補。外部監査に回す |

## 3. 一次資料との比較

「確認箇所」は、各資料の全証明を逐行監査したという意味ではない。

| 一次資料 | 確認箇所・内容 | 候補との関係 |
|---|---|---|
| Adriaensen et al., *Hat guessing with proper colorings*, [arXiv:2603.04909v4](https://arxiv.org/html/2603.04909v4), 2026-08-24 | モデル、clique 定理、一般上界、Table 1、§7。Table 1 の hourglass は \(5\le\mathrm{HG}_P\le7\)。§7 は windmill を今後の評価対象に挙げる | 今回の厳密値6と直接比較できる基準。これだけで後続文献の不存在は言えない |
| He–Ido–Przybocki, *Hat Guessing on Books and Windmills*, [arXiv:2010.13249v1](https://arxiv.org/html/2010.13249v1), [EJC 29(1), P1.12 (2022)](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v29i1p12) | 通常ゲームのモデル、windmill の定義、§4 の構成・上界 | 同じグラフ族で通常ゲームの値は \(r\ge2\) で4。proper 制約の6や7にそのまま読み替えることはできない |
| Alon–Chizewer, *On the Hat Guessing Number of Graphs*, [arXiv:2107.05995v2](https://arxiv.org/html/2107.05995v2) | 通常ゲームで、中心部の複数配置を固定し、各外側の対を同時に失敗させる計数的上界 | 今回の上界の証明構図に先例がある。グラフも許される配置も異なり、今回の数値を直接述べない |
| Latyshev–Kokhas, *The Hats game. The power of constructors*, [arXiv:2102.07138v1](https://arxiv.org/html/2102.07138v1) | constructor / product と §2.3 の windmill 結果 | 通常ゲーム・頂点別 palette の構成。proper coloring の値6を直接与える定理は確認できなかった |
| Chizewer–McInnis–Sohrabi–Kaistha, cactus / cycles 論文, [arXiv:2312.00928v1](https://arxiv.org/html/2312.00928v1) | モデル、冒頭の cactus 分類定理 | 三角形を2個以上含む cactus の通常ゲームの値4は既知。「proper subgame」は proper coloring と同義ではない |
| McInnis, *Slavic Techniques for Hat Guessing Algorithms*, [arXiv:2507.21487v1](https://arxiv.org/html/2507.21487v1), 2025年公開・本文は2023年の学位論文 | 全文の語句検索、ゲーム定義、bowtie の記述、§3.2 の hints / completion 周辺 | 通常の独立な帽子配置を扱う。bowtie の4や completion の先例はあるが、今回と同じ proper 制約の6・閾値3は確認できなかった |
| Zhai, *Proper Hat-Guessing on Two-Spine Book Graphs*, [arXiv:2607.25274v3](https://arxiv.org/html/2607.25274v3), 2026-08-18 | モデル、主要定理、§3 の target / guarding / coverability | proper ゲームで近い補完法が既存。対象は \(K_k\vee\overline K_n\) で、周辺は独立集合。今回の \(K_1\vee(rK_2)\) とは異なる |
| Kakatelis, *An upper bound on the proper hat guessing number of graphs*, [arXiv:2610.04124v2](https://arxiv.org/pdf/2610.04124), 2026-10-06 | 導入、Theorem 1.1、全文の対象語検索 | 現在の \(n,\Delta\) 一般上界も比較した。下記の代入では6・7の小さい厳密値は出ない |
| Matthew Protti の [公開研究リポジトリ](https://github.com/matthewprotti/proper-hat-guessing-k5-minus-e), 2026年9月の公開資料 | root README、一般 reduction、K6−e / K7−e / K8−e の各 README | \(K_n-e\) の構成と補完法。今回のグラフの結果と混同しない。README の範囲を確認したもので全添付証明・プログラムを監査したものではない |

Protti の資料は査読済み論文として扱わず、公開済みの先行開示として比較対象に含めた。原論文の表に残った全項目を、そのまま未解決リストとして採用していない。

## 4. 一般定理の単純な帰結か

\(F_r\) では \(n=2r+1,\ \chi=3,\ \Delta=2r\)。

既知の \(\mathrm{HG}_P(G)\le n+\chi(G)-1\) と、Kakatelis の Theorem 1.1

\[
\mathrm{HG}_P(G)\le
\frac32+\Delta+
\frac{\sqrt{2n^2+2n\Delta-10n+9}}2
\]

に代入すると次のとおり。計算は本調査で行った。

| グラフ | \(n+\chi-1\) の上界 | Kakatelis の上界 | 今回の候補値 |
|---|---:|---:|---:|
| \(F_2\) | 7 | 9 | 6 |
| \(F_3\) | 9 | 13 | 7 |

通常ゲームの \(\mathrm{HG}(F_r)=4\) と既知の比較式
\(\mathrm{HG}_P(G)<\chi(G)(\mathrm{HG}(G)+1)\)
を組み合わせても、\(r\ge2\) で整数上界14までである。

したがって、確認したこれらの一般定理への直接代入だけでは、候補定理の核心は得られない。ほかのすべての定理から導けないと主張するものではない。

## 5. 新規性を弱める具体的な帰結：21個なら7

**以下は既存論文の記載そのものではなく、既知結果から今回こちらで導いた帰結。**

Adriaensen et al. §7 は、各人が \(m\) 回推測できる proper ゲームの \(K_n\) で、\((m+1)n-1\) 色の勝利戦略があると述べる。\(n=2,m=2\) なら、5色の \(K_2\) で各頂点2回推測できる。

これを使うと、7色・三角形21個の戦略が作れる。

1. 7色の各非順序対 \(\{a,b\}\) に専用の三角形を1個用意する。対の数は \(\binom72=21\)。
2. その三角形の外側の2頂点に、残る5色上の \(K_2\) の2回推測戦略を割り当てる。
3. 各頂点の2個の推測を順序付け、中心が \(a\) の場合は第1推測、\(b\) の場合は第2推測を使わせる。中心が他色の場合や、隣の葉の色がその5色に含まれない入力の規則は、合法な推測で任意に埋める。
4. 同じ外側の見え方で、中心色 \(a,b\) の両方について全周辺頂点が失敗することはない。もし両方失敗すれば、専用の対で元の2回推測戦略の全4推測が失敗し、矛盾する。従って全周辺が失敗した見え方では中心候補が高々1色となり、中心が補完できる。

よって既知の複数推測結果と基本的な中心補完から \(\mathrm{HG}_P(F_{21})\ge7\) が従う。

また8色に対する初等的な障害は次のとおり。中心候補を2色固定すると、各外側の対に残る色は6色、合法な順序付き配置は30個。2中心候補×2頂点の4個の正解事象は各々高々6配置、合計高々24配置しか覆えない。そこで各三角形で両中心候補に共通する失敗配置を選べる。中心には同一の見え方しか与えられず、両候補を1回で正解できない。

したがって「十分多数なら値7に安定する」という存在主張だけでは、新規性は弱い。**21個から最小3個への到達個数の決定と、直前の2個で6であることを中心に据える。**

## 6. 検索範囲と本文での照合

二つの検索エンジンで、以下の語群を組み合わせた。新しい proper-game 文献、参照文献、著者公開資料も追った。

- proper hat guessing / proper hat-guessing / proper colouring / proper coloring
- friendship graph(s), Dutch / triangular windmill, \(W_{3,n}\)
- hourglass, bowtie, bow-tie, butterfly
- cactus, block graphs, bouquet、中心共有の三角形、small exact cases

加えて、下記4本の取得本文全体に対象語の機械検索を行い、該当箇所と上記の関連節を読んだ。これは全証明の逐行精査とは区別する。

| 本文 | friendship | windmill | hourglass | bowtie / bow-tie | 文脈 |
|---|---:|---:|---:|---:|---|
| 2603.04909v4 | 0 | 2 | 1 | 0 | hourglass の既知区間、windmill の今後の課題、参考文献 |
| 2607.25274v3 | 0 | 1 | 0 | 0 | windmill は参考文献 |
| 2507.21487v1 | 0 | 5 | 0 | 3 | 通常ゲームの windmill / bowtie、参考文献 |
| 2610.04124v2 | 0 | 1 | 0 | 0 | windmill は参考文献 |

語の不在だけを新規性の根拠にせず、モデル・グラフ・定理の帰結を比較した。検索未収録資料、別表現の結果、非公開研究まで排除した判定ではない。

## 7. 監査状態と推奨する原稿の立て方

| 項目 | 状態 |
|---|---|
| 同一の数式・厳密値・最小閾値を述べる先行結果 | 今回の検索では未発見 |
| 既知の一般定理への直接代入で核心が出るか | 上記の比較では出ない |
| モデル・completion・計数手法そのものの新規性 | 主張しない |
| 新規性の確定 | INCONCLUSIVE |
| 数学的証明・有限検証 | v0.1 の内部監査結果を引き継ぐ。本検索は外部証明監査の代わりではない |
| 外部レビュー | PENDING |
| 公開・投稿 | HOLD |

原稿は「proper windmill の新しいモデル／補完法」ではなく、**friendship graphs の厳密値と sharp three-triangle threshold** を主題にする。関連研究には通常 windmill、proper-coloring の導入、proper books の補完法を入れ、clique の5は既知として扱う。

このメモは独立した新規性監査の追補であり、先に作成した v0.1 の証明・検証パッケージを変更しない。次のレビューでは、特に \(F_2\) の7色不可能証明と \(F_3\) の7色構成を、任意の頂点別戦略を許すモデルで照合する。

