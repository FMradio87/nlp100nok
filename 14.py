from sys import argv

base = argv[1]

N = int(input('何行？-'))

with open(argv[1]) as base_file:
    for i,text in enumerate(base_file,1):
        if i > N:
            break

        print(text.rstrip())