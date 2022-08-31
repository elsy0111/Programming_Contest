import ast
import requests as rq
import json
import os

#import re
base_url = "https://procon33-practice.kosen.work/"
api_token = "9ac59dd7f7034eb595d3b02786b5d5d67bdef0dab72f67ab6c359cba7713eeac"
send_dic = {"procon-token":api_token}
def get_game():
    r = rq.get(base_url+"match" , headers=send_dic)
    print(r.text)
    print(r.status_code)

def get_problem():
    r = rq.get(base_url+"problem" , headers=send_dic)
    print(r.text)
    print(r.status_code)

def post_split(n):
    #wavの保存がまだ
    r = rq.post(base_url+"problem/chunks?n="+str(n) , headers=send_dic)
    print(r.text)
    texture = r.text
    result = ast.literal_eval(texture)
    texture = list(result["chunks"])
    print(texture)
    for i in texture:
        print(i)
        r = rq.get(base_url+"problem/chunks/"+i , headers=send_dic)
        file = open(os.path.join("./audio" , os.path.basename(base_url+"problem/chunks/"+i)), "wb")

        for chunk in r.iter_content(1000000):
            file.write(chunk)
        print(r.status_code)

def send_answer(problem , a_list):
    #problem=問題番号(get_problemで取得できる),a_list=読みデータ番号のリスト
    send_dic.update({"Content-Type" : "application/json"})
    send_json = {
        "problem_id" : problem ,
        "answers" : a_list
    }
    r = rq.post(base_url+"problem",headers=send_dic,data=json.dumps(send_json))
    print(r.text)
    print(r.status_code)

post_split(2)