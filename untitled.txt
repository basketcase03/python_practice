import sys

filename=sys.argv[1]
word=sys.argv[2]


for line in open(filename).readlines():
    words=line.split()
    if word in words:
        print(line)
