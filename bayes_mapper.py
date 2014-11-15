#!usr/bin/python
# python bayes_mapper.py < split2_small_train.txt > counts_small_train.txt

import sys

for line in sys.stdin:
    line = line.strip()
    values = line.split('\t')
    print len(values)
    if len(values) == 28:
        if values[0] == "train":
            features = [values[1]]
            features.extend(values[5:20])
            print '\t'.join(features)
