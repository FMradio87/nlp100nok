f = 'hightemp.txt'

with open(f) as text0, open('col1.txt','w') as text1, open('col2.txt','w') as text2:
    list = text0.readlines()
    for base in list:
        bun = base.split('\t')
        text1.write(bun[0] + '\n')
        text2.write(bun[1] + '\n')
    print(text1.rstrip('\n'))
    print(text2.rstrip('\n'))