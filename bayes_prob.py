#!/usr/bin/python
# python bayes_prob.py < bcounts_small_train.txt > bprob_small_train.txt

# cat $(ls -t) > avazu-train.txt
# python bayes_prob.py < ./data/out4/avazu-train.txt > bprob-avazu-train.txt

import sys

fields = ["banner_pos", "site_id", "site_domain", "site_category", "app_id","app_domain", "app_category", "device_id", "device_ip", "device_os", "device_make", "device_model", "device_type", "device_conn_type", "device_geo_country"]

counts = {"0": {"total": 0.0}, "1": {"total": 0.0}}
for i in range(0, 15):
    counts["0"][fields[i]] = {"feature_ct": 0.0, "strange": 0.0}
    counts["1"][fields[i]] = {"feature_ct": 0.0, "strange": 0.0}
    
for line in sys.stdin:
    line = line.strip()
    values = line.split('\t')
    if len(values) == 4:
        click, feature, cat, count = values
        ct = float(count)
        if feature != "total":
            counts[click][feature]["feature_ct"] += ct
            if ct < 6:
                counts[click][feature]["strange"] += ct
            else:
                counts[click][feature][cat] = ct
        else:
            counts[click]["total"] += ct

prob_click = counts["1"]["total"] / (counts["1"]["total"] + counts["0"]["total"])
            
for click in counts:
    for feature in counts[click]:
        if feature != "total":
            feature_ct = counts[click][feature]["feature_ct"]
            # unique # of categories in feature. subtract "feature_ct" & "strange"
            unique_cat = len(set(counts[click][feature].keys())) - 2
            for cat in counts[click][feature]:
                if cat != "feature_ct":
                    cat_ct = counts[click][feature][cat]
                    # +1 and +1 unique_cat bc we want probabilities with smoothing
                    prob = (cat_ct + 1) / (feature_ct + unique_cat)
                    print "%s\t%s\t%s\t%s\t%s" % (click, feature, cat, prob, cat_ct)
                else:
                    print "%s\t%s\t%s" % (click, feature, feature_ct)
        else:
            if click == '0':  
                print "%s\t%s\t%s\t%s" % (click, feature, (1.0 - prob_click), counts[click]["total"])
            else:
                print "%s\t%s\t%s\t%s" % (click, feature, prob_click, counts[click]["total"])
