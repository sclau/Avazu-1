#!/usr/bin/python
# python train_split_mapper.py < small_train.txt > split1_small_train.txt

import sys

for linenum, line in enumerate(sys.stdin):
    if linenum != 0:
        line = line.strip()
        vals = line.split(',')
        print '\t'.join(vals)
