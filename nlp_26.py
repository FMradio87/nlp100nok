'''
26.強調マークアップの除去
25の処理時に、テンプレートの値からMediaWikiの強調マークアップ（弱い強調、強調、強い強調）を全て除去してテキストに変換せよ
'''

import re
import nlp_25

#強い強調とは？
reference_data = nlp_25.data2

for retult in reference_data:
    Emphasis = re.sub(r'[\']', (''), retult)
    print(Emphasis)
