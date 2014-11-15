#!usr/bin/python
# python bayes_prob.py < bcounts_small_train.txt

import sys

counts = {"0": {}, "1": {}}
for i in range(0, 15):
    counts["0"][str(i)] = {"feature_ct": 0.0, "strange": 0.0}
    counts["1"][str(i)] = {"feature_ct": 0.0, "strange": 0.0}
    
for line in sys.stdin:
    line = line.strip()
    values = line.split('\t')
    if len(values) == 4:
        click, feature, cat, count = values
        ct = float(count)
        counts[click][feature]["feature_ct"] += ct
        if ct < 6:
            counts[click][feature]["strange"] += ct
        else:
            counts[click][feature][cat] = ct
                
    elif len(values) == 3:
        click, total, count = values
        if total == "total":
            counts[click]["total"] = float(count)

prob_click = counts["1"]["total"] / (counts["1"]["total"] + counts["0"]["total"])
            
for click in counts:
    for feature in counts[click]:
        if feature != "total":
            feature_ct = counts[click][feature]["feature_ct"]
            for cat in counts[click][feature]:
                if cat != "feature_ct":
                    cat_ct = counts[click][feature][cat]
                    prob = cat_ct / feature_ct
                    print "%s\t%s\t%s\t%s\t%s" % (click, feature, cat, prob, cat_ct)
                else:
                    print "%s\t%s\t%s" % (click, feature, feature_ct)
        else:
            if click == '0':  
                print "%s\t%s\t%s\t%s" % (click, feature, prob_click, counts[click]["total"])
            else:
                print "%s\t%s\t%s\t%s" % (click, feature, (1.0 - prob_click), counts[click]["total"])
