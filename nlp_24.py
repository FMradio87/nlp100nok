import json
import gzip
import re

def fetch_uk_data():
    with gzip.open('jawiki-country.json.gz',"rt") as js_file:
        for line in js_file:
            js_data = json.loads(line)
            if js_data["title"] == "イギリス":
                return js_data["text"]

file = re.compile(r'^.*(ファイル:.*?\|).*$',re.MULTILINE + re.VERBOSE)

date = file.findall(fetch_uk_data())
for result in date:
    print(result)