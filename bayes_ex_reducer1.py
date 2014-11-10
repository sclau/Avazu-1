#!/usr/bin/python
# python bayes_ex_reducer1.py < counts_small_train.txt > bayes1_small_train.txt

import sys

counts = {}
for i in range(0, 15):
    counts[str(i)] = {}

for line in sys.stdin:
    line = line.strip()
    click, feature, cat, num = line.split('\t')
    if click == '1':
        if cat in counts[feature]:
            counts[feature][cat] = float(num)
        else:
            counts[feature][cat] = {}
            counts[feature][cat] = float(num)
        
feature_cts = {}
for feature in counts:
    for cat in counts[feature]:
        if feature in feature_cts:
            feature_cts[feature] += counts[feature][cat]
        else:
            feature_cts[feature] = counts[feature][cat]
        
for feature in counts:
    for cat in counts[feature]:
        cat_count = counts[feature][cat]
        try:
            prob = counts[feature][cat] / feature_cts[feature]
        except ZeroDivisionError:
            prob = ''
        print "%s\t%s\t%s\t%s" % (feature, cat, prob, cat_count)
        