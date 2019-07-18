'''
29.国旗画像のURLを取得する
テンプレートの内容を利用し、国旗画像のURLを取得せよ。
（ヒント：MediaWiki APIのimageinfoを呼び出して、ファイル参照をURLに変換すれば良い）
'''
#書き換えじゃなくて参照して表示？
#国旗画像のURLとは？？？（国旗のとこにあるやつ）
import re
import json
import requests
from nlp_20 import fetch_uk_data


temple = re.compile(r'^\|(.+?)\s*=\s*(.+?)$',re.MULTILINE)
base = temple.findall(fetch_uk_data())

diction ={}

for fields in base:
    diction[fields[0]] = fields[1]

flag = diction['国旗画像']

print(flag)