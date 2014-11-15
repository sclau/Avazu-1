#!usr/bin/python
# python bayes_reducer.py < counts_small_train.txt > bcounts_small_train.txt

import sys

counts = {0: {}, 1: {}}
for i in range(0, 15):
    counts[0][i] = {}
    counts[1][i] = {}

for line in sys.stdin:
    line = line.strip()
    values = line.split('\t')
    if len(values) == 16:
        features = values[1::]
        # no click
        if values[1] == '0':
            for i, feat in enumerate(features):
                if feat in counts[0][i]:
                    counts[0][i][feat] += 1
                else:
                    counts[0][i][feat] = 1
            # total count of non clicks
            if "total" in counts[0]:
                counts[0]["total"] += 1
            else:
                counts[0]["total"] = 1
                    
        # click
        elif values[1] == '1':
            for i, feat in enumerate(features):
                if feat in counts[1][i]:
                    counts[1][i][feat] += 1
                else:
                    counts[1][i][feat] = 1 
            # total count of clicks
            if "total" in counts[1]:
                counts[1]["total"] += 1
            else:
                counts[1]["total"] = 1

for click in counts:
    for feature in counts[click]:
        if feature != "total":
            for cat in counts[click][feature]:
                cat_count = counts[click][feature][cat]
                print "%s\t%s\t%s\t%s" % (click, feature, cat, cat_count)
        else:
            print "%s\t%s\t%s" % (click, feature, counts[click][feature])
            