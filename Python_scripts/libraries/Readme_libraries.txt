get_and_post.pyの使い方
from libraries.get_post import *
のように書けばPython_Scripts直下にあるプログラムであれば
モジュールとして組み込める(Python_Scriptsより下にあったら無理)
※__pycache__は消さなくていいかも

1. get_game()
get_game()すれば試合情報がわかる

2. get_problem()
get_problem()すれば問題の情報が手に入る
send_answerメソッド内にこの関数を埋め込む関係上
問題idを返り値とするが、変数に代入する必要はない

3. post_split(n)
これはnのところに任意の整数を入れれば
・取得する分割データ数の情報を送信
・分割データの読み込み
までを1セットで行う
関数そのものは返り値を持たず、wavファイルをPython_scripts/audioの中に
そのまま入れるタイプ

4. send_answer(a_list)
導き出した答えをサーバーに送る
a_listには答えとなる読みデータを
リスト化したやつを入れていただければ○ 例:send_answer([1,2,23,42])
※a_listはintで入れて一桁の場合は0埋めしない(1を01としない)

tidy_output.pyの使い方
from libraries.tidy_output from *
(もしくはfrom libraries.tidy_output from make_answer_list)でimportする
送信するリストを格納したい変数に代入して
第一引数に整形前のnumpyの配列、第二引数に含まれている読みデータ数を渡す
そうすると整形された配列が変数の中に格納されているので
send_answerに渡してあげれば送信される