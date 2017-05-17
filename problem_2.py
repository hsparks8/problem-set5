#! usr/bin/env python3

# 2. total number of c bases in fastq

from collections import Counter
count = 0
bases = Counter()

import sys

filename = sys.argv[1]

for line in open(filename):
    line = line.rstrip()
    if count == 0:
        name = line
        count += 1

    elif count == 1:
        seq = line
        count += 1

    elif count == 2:
        count += 1

    elif count == 3:
        qual = line
        count = 0

        for base in seq:
            bases[base] += 1

print(bases['C'])

