#!/usr/bin/python
# given the training set, compute the predicted values for each validation instance

from operator import mul
import sys
import os.path
sys.path.append(os.path.dirname(__file__))

fields = ["hour", "C1", "banner_pos", "site_id", "site_domain", "site_category", "app_id", "app_domain", "app_category", "device_id", "device_ip", "device_model", "device_type", "device_conn_type", "C14", "C15", "C16", "C17", "C18", "C19", "C20", "C21"]  #list of features

keep_fields = ["banner_pos", "site_category", "app_category", "device_type", "ad_size"]


def read_probs():
	# Same code that professor used in Naive Bayes
	probs = {}
	with open("bayes_probs_base_2.txt", "r") as f:
		lines = f.readlines()
	for line in lines:
		line = line.strip()
		feature, value, prob_click, prob_no_click = line.split('\t')
		key = "%s,%s" % (feature,value)
		probs[key] = (float(prob_click), float(prob_no_click))
	return probs

prob_dict = read_probs()  # prob_dict now a dictionary with all the probabilities 
pclick, pnclick = prob_dict["Total,Total"]

for line in sys.stdin:
    line = line.strip()
    words = line.split(",")
    if len(words) == 24 and words[0] != "id":
        feat = dict(zip(fields, words[2::]))
        day = feat["hour"][-4:-2]   #extract the day out of the date variable
        if day == "29" or day == "30":  #then it is validation
            click_prob_list = [pclick]  # store P(Click) first
            no_click_prob_list = [pnclick]  # store P(No-Click)
            feat["hour"] = feat["hour"][-2::]  # get hours from date
            
            # combine C15 and C16 into ad size
            feat["ad_size"] = feat["C15"] + "x" + feat["C16"]
            
            features = {}
            for key in feat:
                if key in keep_fields:
                    features[key] = feat[key]
            
            # remove unknown values for features
            if features["site_category"] == "50e219e0":
                features.pop("site_category", None)
            if features["app_category"] == "07d7df22":
                features.pop("app_category", None)
            
            for feature in features:
                value = features[feature]
                key = "%s,%s" % (feature, value)  # use this key to look into dictionary
                if key in prob_dict:  # if key in dictionary, use the conditional probabilities
                    click_prob_list.append(prob_dict[key][0])
                    no_click_prob_list.append(prob_dict[key][1])
                else:  # otherwise consider it a strange (UNK) value
                    key = "%s,%s" % (feature, "strange")
                    no_click_prob_list.append(prob_dict[key][1])
                    click_prob_list.append(prob_dict[key][0])
            # P(cat1 | Click)*...*P(cat_k | Click)*P(Click)
            click_product = reduce(mul, click_prob_list) 
            # P(cat1 | No Click)*...*P(cat_k | No Click)*P(No Click)
            no_click_product = reduce(mul, no_click_prob_list) 
            denominator = click_product + no_click_product
            predict_prob = float(click_product)/denominator
            # outputs <id>, <type>, <predict_prob>
            print '%s\t%s\t%s' %  (words[0], "pred", predict_prob)
            print '%s\t%s\t%s' %  (words[0], "act", words[1])