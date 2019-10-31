'''
32.動詞の原形
動詞の原形を全て抽出せよ.
'''
import nlp_30


base =nlp_30.base_file()

verbs = set()
verbs_test = []

for line in base:
    if line['pos'] == '動詞':
        verbs.add(line['base'])
        verbs_test.append(line['base'])

print(sorted(verbs, key=verbs_test.index))