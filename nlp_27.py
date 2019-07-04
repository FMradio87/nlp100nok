'''
27.内部リンクの除去
26の処理に加えてテンプレートの値からMediaWikiの内部リンクマークアップを除去し、テキストに変換せよ
'''

import re
import nlp_26

#リンクマークアップは[[,|,]]だと思うからそれをsubで置換する

refarence_data2 = nlp_26

link_mark = re.sub(r'[\[\[],[\|],[\]\]]',(''),refarence_data2)

print(link_mark)