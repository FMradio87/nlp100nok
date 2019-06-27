f = 'hightemp.txt'

with open(f) as l:
    for i in l:
        print(i.replace('\t',' '), end='')