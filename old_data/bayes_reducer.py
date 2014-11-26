#!/usr/bin/python
# sort counts_small_train.txt -k1,1 -o counts_small_train.txt 
# python bayes_reducer.py < counts_small_train.txt > bcounts_small_train.txt

from operator import itemgetter
import sys

current_feature_combo = None
feature_combo = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    feature_combo, count = line.split("\t")
    try:
        count = int(count)
    except ValueError:
        continue
    
    if current_feature_combo == feature_combo:
        current_count += count
    else:
        if current_feature_combo:
            click, feature, cat = current_feature_combo.split(".")
            print "%s\t%s\t%s\t%s" % (click, feature, cat, current_count)
        current_count = count
        current_feature_combo = feature_combo
        
if current_feature_combo == feature_combo:
    click, feature, cat = current_feature_combo.split(".")
    print "%s\t%s\t%s\t%s" % (click, feature, cat, current_count)