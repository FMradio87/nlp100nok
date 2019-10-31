'''
31.動詞
動詞の表層形を全て抽出せよ.
（動詞のやつを抜き出して、それの表層形をリストに入れたらオッケー？）
'''
import nlp_30


base =nlp_30.base_file()

verbs = set()
verbs_test = []

for line in base:
    if line['pos'] == '動詞':
        verbs.add(line['surfase'])
        verbs_test.append(line['surfase'])


print(sorted(verbs, key=verbs_test.index))

#ただverdsですると出力結果が毎回違ってしまう…
