'''
27.内部リンクの除去
26の処理に加えてテンプレートの値からMediaWikiの内部リンクマークアップを除去し、テキストに変換せよ
'''

import re
import nlp_25

#リンクマークアップは[[,|,]]だと思うからそれをsubで置換する
refarence_data2 = nlp_25.data2


for retult in refarence_data2:
    Emphasis = re.sub(r'[\']', (''), retult)
    i = re.sub(r'(\|)', (''), Emphasis)
    i2 = re.sub(r'(\[)', (''), i)
    i3 = re.sub(r'(\])', (''), i2)
    i4 = re.sub(r'(\|)', (''), i3)
    retult3 = re.findall('=\s(.*)', i4)

    for au in retult3:
        if i:
            retult2 = au
            print(retult2)