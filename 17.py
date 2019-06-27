from sys import argv
import collections

base = argv[1]

with open(argv[1]) as base_file:
    line = base_file.readlines()

    col = collections.Counter(line[0])

    print(len(set(col)))

    print(set(col))