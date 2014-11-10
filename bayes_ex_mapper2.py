#!/usr/bin/python
# python bayes_ex_mapper2.py < bayes1_small_train.txt > bayes2_small_train.txt

import sys

pooled = {}
for i in range(0, 15):
    pooled[str(i)] = {"feature_ct": 0.0, "strange": 0.0}
    
for line in sys.stdin:
    line = line.strip()
    feature, cat, prob, count = line.split('\t', 4)
    count = float(count)
    pooled[feature]["feature_ct"] += count
    
    if count < 2:
        pooled[feature]["strange"] += count    
    else:
        print "%s\t%s\t%s\t%s" % (feature, cat, prob, count)

for feature in pooled:
    for cat in pooled[feature]:
        print "%s\t%s\t%s\t%s" % (feature, cat , 0.0, pooled[feature][cat])
    