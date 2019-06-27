from sys import argv
import collections

base = argv[1]

with open(argv[1]) as base_file:
    line = base_file.readlines()

    col = collections.Counter(line)

    col2 = col.sorted(key=lambda s:s[0])

    print(col2)

