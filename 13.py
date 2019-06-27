with open('col1.txt') as text1,open('col2.txt') as text2, open('marge.txt','w') as text3:
    for text_1,text_2 in zip(text1,text2):
        text3.write(text_1.rstrip() + '\t' + text_2.rstrip() + '\n')

    print(text3)