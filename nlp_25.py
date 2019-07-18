'''
25.テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ
'''


import json
import gzip
import re

def fetch_uk_data():
    with gzip.open('jawiki-country.json.gz',"rt") as js_file:
        for line in js_file:
            js_data = json.loads(line)
            if js_data["title"] == "イギリス":
                return js_data["text"]


temple = re.compile(r'^\{\{基礎情報.*?(.*?)\}\}$',re.MULTILINE + re.VERBOSE + re.DOTALL)
data = temple.findall(fetch_uk_data())

temple2 = re.compile(r'^\|(.+?)\s*=\s*(.+?)$',re.MULTILINE + re.DOTALL + re.VERBOSE)

base = temple2.findall(data[0])

diction = {}

for field in base:
    diction[field[0]] = field[1]

print(diction)