'''
20.JSONデータの読み込み
Wikipedia記事のJSONファイルを読みこみ、「イギリス」に関する記事本文を表示せよ。
問題２１−２９では、ここで抽出した記事本文に対して実行せよ
'''

import json
import gzip

def fetch_uk_data():
    with gzip.open('jawiki-country.json.gz',"rt") as js_file:
        for line in js_file:
            js_data = json.loads(line)
            if js_data["title"] == "イギリス":
                return js_data["text"]
if __name__== '__main__':
    print(fetch_uk_data())


#名前をnlp_20.pyとかにすればいけるかな？