'''
21.カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ
'''

import json
import gzip
import re

def fetch_uk_data():
    with gzip.open('jawiki-country.json.gz',"rt") as js_file:
        for line in js_file:
            js_date = json.loads(line)
            if js_date["title"] == "イギリス":
                return js_date["text"]

category = re.compile(r'^\[\[Category:.*\]\]$',re.MULTILINE + re.VERBOSE)

data = category.findall(fetch_uk_data())

for result in data:
    print(result)