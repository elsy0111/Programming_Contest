get_and_post.pyの使い方
from get_post.get_and_post import *
のように書けばPython_Scripts直下にあるプログラムであれば
モジュールとして組み込める(Python_Scriptsより下にあったら無理)

1. get_game
何も考えずにget_game()しとけば試合情報がわかる

2. get_problem
これも何も考えずにget_problem()しとけば問題の情報が手に入っちゃう
まるで今の情報社会を風刺しているかのよう

3. post_split(n)
これはnのところに任意の整数を入れれば
・取得する分割データ数の情報を送信
・分割データの読み込み
までを1セットで行うやつ
関数そのものに返り値を持ってるわけじゃなくてwavファイルをPython_scripts/audioの中に
ばーん！！！！！！！！って入れるタイプ
まだ実装してないけど音声ファイル名のリストを返り値にしたら
スムーズになっていいのかも

4. send_answer(problem,a_list)
導き出した答えをサーバーに送ってくれる
problemにはget_problemで取得した問題ID,a_listには答えとなる読みデータを
リスト化したやつを入れていただければ○ (例:send_answer("qual-1-1" , ["01","02"]))