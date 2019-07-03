import json
import gzip
import re

def fetch_uk_data():
    with gzip.open('jawiki-country.json.gz',"rt") as js_file:
        for line in js_file:
            js_data = json.loads(line)
            if js_data["title"] == "イギリス":
                return js_data["text"]


temple = re.compile(r'^\{\{基礎情報.*?\}\}$',re.MULTILINE + re.VERBOSE + re.DOTALL)
data = temple.findall(fetch_uk_data())
data2 = data[0].split('\n')

temple2 = re.compile(r'\|(?P<field>.+) = (?P<value>.+)')


for base in data2:
     m = temple2.match(base)
     if m:
        print(m.groupdict())

