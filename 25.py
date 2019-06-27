import json
import gzip
import re

def fetch_uk_data():
    with gzip.open('jawiki-country.json.gz',"rt") as js_file:
        for line in js_file:
            js_data = json.loads(line)
            if js_data["title"] == "イギリス":
                return js_data["text"]


temple = re.compile(r'^{{基礎情報(|.*)\s*(=)\s*(.*)}}$',re.MULTILINE + re.VERBOSE)

data = temple.findall(fetch_uk_data())

for result in data:
    field = result[0]
    value = result[2]
    print(field)
    #print(value)
#フィールド名（|.*" "）かな？
#値　難しい、おそらく（＝の後の分？）ってことかな？
#基礎情報自体は{{基礎情報-  }}で取れば出てくる？