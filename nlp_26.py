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
reference_data = nlp_25.m

Emphasis = re.sub(r'[\']',(''),reference_data)


print(Emphasis)