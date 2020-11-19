# 概要
研究室で管理しているサーバ一覧の情報です．
サーバの固定ipは別ページ [ipアドレス.md](ipアドレス.md)  を参照．

### 組み込み系
| 名前        | 役割           | OS           | 機器                    | 設置場所         | 外部IP | 備考             |
| ----        | ----           | ----         | ---                     | ----             | -----  | --               |
| syn         | ルータ         | 組み込み     | RTX1200                 | 学生部屋         | あり   |                  |
| eir         | ポリコム       | 組み込み     | ポリコム                | 輪講室           | あり   |                  |
| aria        | ポリコム       | 組み込み     | ポリコム                | 教授室           | あり   |                  |

### メインサーバ
| 名前        | 役割           | OS           | 機器                    | 設置場所         | 外部IP | 認証方式| 備考             |
| ----        | ----           | ----         | ---                     | ----             | -----  | ---    | --               |
| fenrir      | web鯖          | Ubuntu 16.04 | HP ProLiant DL80 Gen9   | 機器室ラック     | あり   |           |                  |
| hel         | ファイル鯖     | Ubuntu 14.04 | HP ProLiant DL380e Gen8 | 機器室ラック     |        |           |                  |
| loki        | 演習D鯖        | CentOS 7.6   | HP Z840                 | 機器室フルタワー | あり   |           |                  |
| kusuhpc     | 計算用(mem)    | Windows 10   | Fujitsu RX2530 M2       | 機器室ラック     |        |           | 研究科レンタル |
| kvasir      | 計算用(CPU)    | Ubuntu       | 有馬BTO                 | 機器室フルタワー |        |           |                  |
| thor        | 計算用(GPU)    | Ubuntu 18.04 | HP Z840[^specThor]      | 機器室フルタワー |        | 公開鍵, pw | ssh接続 |

[^specThor]: CPU:Xeon(R) E5-2620 v4 GPU:{Tesla K40c, Quadro K2200} mem:128GB

### 旧サーバ
シャットダウン済み，かつ実機が残っているもの

| 名前       | 役割         | OS   | 機器                  | 設置場所     | 外部IP | 備考       |
| ----       | ----         | ---- | ---                   | ----         | -----  | --         |
| ymir       | 旧ファイル鯖 |      | HP ProLiant DL180 G6  | 機器室ラック |        | shutdown済 |
| tyr        | 旧アプリ鯖   |      | HP ProLiant DL320 G6  | 機器室ラック |        | shutdown済, root pw 不明 |
| valkyrie   | 旧アプリ鯖   |      | HP ProLiant DL120 G6  | 機器室ラック |        | shutdown済 |
| fenrir2016 | 旧web鯖      |      | HP ProLiant DL60 Gen9 | 機器室ラック |        | shutdown済 |
