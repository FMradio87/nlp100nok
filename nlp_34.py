'''
34.「AのB」
２つの名詞が「の」で連結されている名詞句を抽出せよ
（AのBという文字列を出す）
'''

import nlp_30


base =nlp_30.base_file()

verbs = set()
verbs_test = []

for line in base:
    if line['pos'] == '名詞' or line['pos1'] == '連体化':
        verbs.add(line['surfase'])
        verbs_test.append(line['surfase'])


#print(sorted(verbs, key=verbs_test.index))

#ただverdsですると出力結果が毎回違ってしまう…

import MeCab

tweet = sorted(verbs, key=verbs_test.index)

tagger = MeCab.Tagger("")

word = []

for tango_list in tweet:
    tab = tango_list.split('\t')
    words = tab[0]
    word.append(words)
#print(word)

three_list = []
for i in range(len(word)-2):
    three_list.append((word[i], word[i+1], word[i+2]))
print(three_list)

import re

a = re.compile('\(.*の.*\)',re.MULTILINE + re.VERBOSE)

data = a.findall(three_list)

print(data)