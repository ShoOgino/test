
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
