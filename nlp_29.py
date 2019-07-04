'''
29.国旗画像のURLを取得する
テンプレートの内容を利用し、国旗画像のURLを取得せよ。
（ヒント：MediaWiki APIのimageinfoを呼び出して、ファイル参照をURLに変換すれば良い）
'''
#sub?を使って書き換えを行えばいいのかな？
#国旗画像のURLとは？？？
import re
import nlp_25

base = nlp_25.data2

for i in base:
    flag_file = re.search(r'Flag\sof\sthe\sUnited\sKingdom\.svg',i)
    if flag_file:
        print(flag_file.group(0))