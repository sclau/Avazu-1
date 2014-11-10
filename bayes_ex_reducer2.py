#!/usr/bin/python
# python bayes_ex_reducer2.py < bayes2_small_train.txt > bayes3_small_train.txt

import sys

pooled = {}
for i in range(0, 15):
    pooled[str(i)] = {"strange": 0.0, "feature_ct": 0.0}
    
for line in sys.stdin:
    line = line.strip()
    feature, cat, prob, count = line.split('\t', 4)
    if cat == "strange":
        pooled[feature]["strange"] = float(count)
    elif cat == "feature_ct":
        pooled[feature]["feature_ct"] = float(count)
    else:
        print "%s,%s,%s,%s" % (feature, cat, prob, count)
        
for feature in pooled:
    strange_ct = pooled[feature]["strange"]
    feature_ct = pooled[feature]["feature_ct"]
    try:
        pool_prob = strange_ct / feature_ct
    except ZeroDivisionError:
        pool_prob = ''
        
    print "%s,%s,%s,%s" % (feature, "strange", pool_prob, strange_ct)
     