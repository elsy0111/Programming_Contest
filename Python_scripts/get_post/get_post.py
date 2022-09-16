import ast
import requests as rq
import json
import os

#import re
base_url = "https://procon33-practice.kosen.work/"
api_token = "9ac59dd7f7034eb595d3b02786b5d5d67bdef0dab72f67ab6c359cba7713eeac"
send_dic = {"procon-token":api_token}
def get_game():
    r = rq.get(base_url+"match" , headers=send_dic,verify=False)
    print(r.text)
    print(r.status_code)

def get_problem():
    r = rq.get(base_url+"problem" , headers=send_dic,verify=False)
    print(r.text)
    texture = r.text
    result = ast.literal_eval(texture)
    p_number = result["id"]
    print(r.status_code)
    return p_number

def post_split(n):
    r = rq.post(base_url+"problem/chunks?n="+str(n) , headers=send_dic,verify=False)
    print(r.text)
    texture = r.text
    result = ast.literal_eval(texture)
    texture = list(result["chunks"])
    print(texture)
    for i in texture:
        print(i)
        r = rq.get(base_url+"problem/chunks/"+i , headers=send_dic,verify=False)
        file = open(os.path.join("./audio" , os.path.basename(base_url+"problem/chunks/"+i)), "wb")

        for chunk in r.iter_content(1000000):
            file.write(chunk)
        print(r.status_code)

def send_answer(a_list):
    #problem=問題番号(get_problemで取得できる),a_list=読みデータ番号のリスト
    send_dic.update({"Content-Type" : "application/json"})
    p_number = get_problem()
    for i,name in enumerate(a_list):
        if a_list[i] < 10:
            a_list[i] = "0"+str(a_list[i])
        else :
            a_list[i] = str(a_list[i])

    send_json = {
        "problem_id" :  p_number ,
        "answers" : a_list
    }

    r = rq.post(base_url+"problem",headers=send_dic,data=json.dumps(send_json),verify=False)
    print(r.text)
    print(r.status_code)