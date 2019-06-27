from sys import argv


with open(argv[1])as f:
    lines = f.readlines()
lines.sort(key=lambda s: float(s.split('\t')[2]), reverse=True)

for line in lines:
    print(line, end='')