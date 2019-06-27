from sys import argv

base = argv[1]

N = int(input('何行？-'))

with open(base) as file_data:
    lines = file_data.readlines()

for i in lines[-N:]:
    print(i.rstrip())