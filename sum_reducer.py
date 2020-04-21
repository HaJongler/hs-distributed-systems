#!/usr/bin/python

import sys
from collections import defaultdict

counts = defaultdict(int)

for line in sys.stdin:
    try:
        title, num_access = line.strip().split("\t")
    except:
        print(line)
        continue
    counts[title] += int(num_access)
    
for title, count in counts.items():
    print(title, count, sep="\t")
