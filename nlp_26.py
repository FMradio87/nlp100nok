'''
26.強調マークアップの除去
25の処理時に、テンプレートの値からMediaWikiの強調マークアップ（弱い強調、強調、強い強調）を全て除去してテキストに変換せよ
'''

import re
import nlp_25

'''def fetch_uk_data():
    with gzip.open('jawiki-country.json.gz',"rt") as js_file:
        for line in js_file:
            js_date = json.loads(line)
            if js_date["title"] == "イギリス":
                return js_date["text"]
'''
#強い強調とは？
reference_data = nlp_25

Emphasis = re.sub(r'[\']',(''),reference_data)


print(Emphasis)