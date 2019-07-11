'''
28.MediaWikiマークアップの除去
27の処理に加えて、テンプレートの値から　MediaWikiマークアップを可能な限り除去し、国の基礎情報を整形せよ。
'''
import nlp_25
import re

#他のマークアップってどれだ…

refarence_data3 = nlp_25.data2

for retult in refarence_data3:
    Emphasis = re.sub(r'[\']', (''), retult)
    i = re.sub(r'(\|)', (''), Emphasis)
    i2 = re.sub(r'(\[)', (''), i)
    i3 = re.sub(r'(\])', (''), i2)
    i4 = re.sub(r'\|', (''), i3)
    i5 = re.sub(r'<\/?(br|ref|references)(.*?)>',(''),i4)
    i6 = re.sub(r'\{\{langen\}\}',(''),i5)
    retult3 = re.findall('=\s(.*)', i6)

    for bu in retult3:
        if i:
            retult2 = bu
            print(bu)




