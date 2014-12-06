fields = ["banner_pos", "site_category", "app_category", "device_type", "ad_size"]

counts = {"0": {"total": 0.0}, "1": {"total": 0.0}}
for i in range(0, len(fields)):
    counts["0"][fields[i]] = {"feature_ct": 0.0, "strange": 0.0}
    counts["1"][fields[i]] = {"feature_ct": 0.0, "strange": 0.0}

with open('data/counts/avazu_train.txt', 'r') as f: 
    for line in f.readlines():
        line = line.strip()
        values = line.split('\t')
        if len(values) == 4:
            click, feature, cat, count = values
            ct = float(count)            
            if feature != "total" and feature in fields:
                counts[click][feature]["feature_ct"] += ct
                counts[click][feature][cat] = ct
            else:
                counts[click]["total"] += ct

to_delete = []                
for click in counts:
    for feature in counts[click]:
        if feature != "total":
            for cat in counts[click][feature]:
                if cat in counts["0"][feature]:
                    nclick_count = counts["0"][feature][cat]
                else:
                    nclick_count = 0.0
                if cat in counts["1"][feature]:
                    click_count = counts["1"][feature][cat]
                else:
                    click_count = 0.0
                count = counts[click][feature][cat]
                total_ct = nclick_count + click_count
                # check if total count for a category is less than 6
                if total_ct <= 300:
                    # add counts to strange
                    counts[click][feature]["strange"] += count
                    # delete category bc integrate
                    if cat != "strange":
                        to_delete.append((click, feature, cat))
                    
# remove counts from dictionary that were added to strange
for i in to_delete:
    click, feature, cat = i
    counts[click][feature].pop(cat, None)
                                
prob_click = counts["1"]["total"] / (counts["1"]["total"] + counts["0"]["total"])

# add categories from no_click feature if seen in click but no no_click and vice versa. necessary for probability smoothing
for click in counts:
    for feature in counts[click]:
        if feature != "total":
            nclick_cats = set(counts["0"][feature])
            click_cats = set(counts["1"][feature])
            # categories to be added to no-click feature
            add_nclick = click_cats - nclick_cats
            # categories to be added to click feature
            add_click = nclick_cats - click_cats
            if add_nclick:    
                for cat in add_nclick:
                    counts["0"][feature][cat] = 0.0
            if add_click:
                for cat in add_click:
                    counts["1"][feature][cat] = 0.0
            
for click in counts:
    for feature in counts[click]:
        if feature != "total":
            feature_ct = counts[click][feature]["feature_ct"]
            # unique # of categories in feature. subtract "feature_ct" & "strange"
            click_set = list(set(counts["0"][feature].keys()))
            nclick_set = list(set(counts["1"][feature].keys()))
            unique_cat = len(set(click_set + nclick_set)) - 2
            for cat in counts[click][feature]:
                if cat != "feature_ct":
                    cat_ct = counts[click][feature][cat]
                    # +1 and +1 unique_cat bc we want probs with smoothing
                    try:
                        prob = (cat_ct + 1) / (feature_ct + unique_cat)
                        print "%s\t%s\t%s\t%s\t%s" % (click, feature, cat, prob, cat_ct)
                    except ZeroDivisionError:
                        continue
        else:
            # print probability and total counts of click and no-click
            if click == '0':  
                print "%s\t%s\t%s\t%s" % (click, feature, (1.0 - prob_click), counts[click]["total"])
            else:
                print "%s\t%s\t%s\t%s" % (click, feature, prob_click, counts[click]["total"])
