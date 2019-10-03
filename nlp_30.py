'''
30.形態素解析結果の読み込み
形態素解析結果(neko.txt.mecab)を読み込むプログラムを実装せよ.
ただし、各形態素は表層形(surface),基本形(base),品詞(pos),品詞細分類１(pos1)をキーとするマッピング型に格納し、
１文を形態素(マッピング型)のリストとして表現せよ.
第４章の残りの問題では、ここで作ったプログラムを活用せよ
'''
'''
なんか夏休み前にneko.txt.macabを作ってた。
これそのまま使えるかなと思ってやろうとしてるけど失敗してます
できた！？やった！！例外処理を使ったら大丈夫になった！
（c2でエラーが起きる可能性があったからtryで例外はそのまま続けてねってやった）
morphme(形態素) mapping(マッピング)
'''

def base_file():
    morpheme = []
    with open('neko.txt.mecab',mode='r+',encoding='utf-8') as twofile:
        for a in twofile:
            c1 = a.split('\t')
            try:
                c2 = c1[1].split(',')
            except IndexError:
                continue
            mapping = {'surfase': c1[0], 'base': c2[6], 'pos': c2[0], 'pos1': c2[1]}
            morpheme.append(mapping)
    return morpheme

if __name__ == '__main__':
    for b in base_file():
        print(b)