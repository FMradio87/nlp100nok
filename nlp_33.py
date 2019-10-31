'''
33.サ変名詞
サ変接続の名詞を全て抽出せよ.
（30見直したらpos1にサ変接続とか区別としてあった…てっきりそういう組み合わせを自分で作らないといけないのかと思って戦慄した）
'''
import nlp_30


base =nlp_30.base_file()

verbs = set()
verbs_test = []

for line in base:
    if line['pos1'] == 'サ変接続':
        if line['pos'] == '名詞':
            verbs.add(line['base'])
            verbs_test.append(line['base'])


print(sorted(verbs, key=verbs_test.index))