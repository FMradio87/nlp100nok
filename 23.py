import json
import gzip
import re

def fetch_uk_data():
    with gzip.open('jawiki-country.json.gz',"rt") as js_file:
        for line in js_file:
            js_data = json.loads(line)
            if js_data["title"] == "イギリス":
                return js_data["text"]


section = re.compile(r'^(={2,})\s*(.*?)\s*(={2,}).*$',re.VERBOSE + re.MULTILINE)

date = section.findall(fetch_uk_data())

for result in date:
    level = len(result[2])
    sec = result[1]
    print('セクション名: ' + sec )
    print('レベル: ' +str(level))
