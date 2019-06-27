import json
import gzip

with gzip.open('jawiki-country.json.gz',"rt") as js_file:
    for line in js_file:
        js_data = json.loads(line)
        if js_data["title"] == "イギリス":
            print(js_data["text"])
            break



#名前をnlp_20.pyとかにすればいけるかな？