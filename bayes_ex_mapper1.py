#!/usr/bin/python
# python bayes_ex_mapper1.py < small_train.txt > counts_small_train.txt

import sys

counts = {0: {}, 1: {}}
for i in range(0, 15):
    counts[0][i] = {}
    counts[1][i] = {}

for line in sys.stdin:
    line = line.strip()
    values = line.split(',')
    if len(values) == 27:
        features = values[4:19]
        # no click
        if values[1] == '0':
            for i, feat in enumerate(features):
                if feat in counts[0][i]:
                    counts[0][i][feat] += 1
                else:
                    counts[0][i][feat] = 1 
                    
        # click
        elif values[1] == '1':
            for i, feat in enumerate(features):
                if feat in counts[1][i]:
                    counts[1][i][feat] += 1
                else:
                    counts[1][i][feat] = 1 
      
for click in counts:
    for feature in counts[click]:
        for feat in counts[click][feature]:
        # click or not, feature, counts
            print "%s\t%s\t%s\t%s" % (click, feature, feat, counts[click][feature][feat])
            