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

S = requests.Session()
URL = "https://www.mediawiki.org/w/api.php"
TITLE = 'Flag of the United Kingdom.svg'
#print(flag)

PARAMS = {
    'action':'query',
    'titles':'File:Flag of the United Kingdom.svg',
    'prop':'imageinfo',
    'iiprop':'url',
    'format':'json'
}

R = S.get(url=URL,params=PARAMS)
data = R.json()

PAGES = data['query']['pages']

for k,v in PAGES.items():
    print(v['imageinfo'][0]['url'])

#なんかできたぞ…！？　参考にしたページhttps://www.mediawiki.org/wiki/API:Imageinfo
#ちょっと直した。これでURLだけ出るようになったはず…