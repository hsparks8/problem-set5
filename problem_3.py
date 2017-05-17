#! /usr/bin/env python3

#3. most common hexamer


filename = sys.argv[1]

from collections import Counter

count = 0

hex5 = Counter()
hex3 = Counter()

for line in open(filename):
    line = line.rstrip()

    if count == 0:
        seq = line
        count += 1

    elif count == 1:
        seq = line
        count += 1

    elif count == 2:
        count += 1

    elif count == 3:
        qual = line
        count = 0

        hexamer_5 = []
        hexamer_3 = []
        hex_5 = seq[0:6]
        hex_3 = seq[-6:]
        hex5[hex_5] +=1
        hex3[hex_3] += 1

for k, v in hex5.items():
    sortme = [(v,k) for k,v in hex5.items()]
    sortme
    sortme.sort()
    sortme.reverse()
print("Hexamer_5", sortme[0][1])

for k, v in hex3.items():
    sortme = [(v,k) for k,v in hex3.items()]
    sortme
    sortme.sort()
    sortme.reverse()
print("Hexamer_3", sortme[0][1])




