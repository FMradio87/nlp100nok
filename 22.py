import json
import gzip
import re

def fetch_uk_data():
    with gzip.open('jawiki-country.json.gz',"rt") as js_file:
        for line in js_file:
            js_date = json.loads(line)
            if js_date["title"] == "イギリス":
                return js_date["text"]

categori1 = re.compile(r'^.*\[\[Category:(.*?)(?:\]\]|\|).*$',re.MULTILINE + re.VERBOSE)

date = categori1.findall(fetch_uk_data())
for result in date:
    print(result)