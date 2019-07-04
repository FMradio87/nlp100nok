file = 'hightemp.txt'

with open(file) as f:
    a = f.readlines()
    b = len(a)

print(b)
