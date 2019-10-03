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
'''

def base_file():
    L = []
    with open('neko.txt.mecab') as twofile:
        for a in twofile:
            c1 = a.split('\t')
            c2 = c1[1].split(',')
            maping = {'surfase': c1[0],'base': c2[6],'pos': c2[0],'pos1': c2[1]}
            L.append(maping)
        return L

if __name__ == '__main__':
    for a in base_file():
        print(a)