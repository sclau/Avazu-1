#!/usr/bin/python
# python train_split_reducer.py < split1_small_train.txt > split2_small_train.txt

import sys
import random

for line in sys.stdin:
    line = line.strip()
    num = random.random()
    if num <= 0.6:
        bucket = "train"
    elif num > 0.6 and num <= 0.8:
        bucket = "validation"
    else:
        bucket = "test"
    print "%s\t%s" % (bucket, line)