#! /usr/bin/env python3

#1. report number of intervals for each chromosome in lamina.bed

from collections import Counter

filename = sys.argv[1]

for lines in open(filename):
    if lines.startswith('#'): continue
    fields = lines.split('\t')
    chrom = fields[0]
    counts [chrom] += 1

sortme = [(v,k) for k,v in counts.items()]

sortme.sort()

sortme.reverse()

print("Most intervals", sortme[0][1])

