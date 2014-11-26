#!/usr/bin/python

import sys
from operator import mul
import json
 
with open('dict.json', 'rb') as fp:
    feature_dict = json.load(fp)

"""For each line in the validation/test data, create a list of
the relevant probabilities from the dictionary feature_dict,
take products to come up with the numerator and denominator for naive Bayes"""

fields = ["banner_pos", "site_id", "site_domain", "site_category", "app_id","app_domain", 
"app_category", "device_id", "device_ip", "device_os", "device_make", "device_model", 
"device_type", "device_conn_type", "device_geo_country"]

for line in sys.stdin:
	line = line.strip()
	words = line.split("\t")
	if len(words) == 28 and words[0] == "validation":
  		click_probs_list = [float(feature_dict["click_prob"]["1"])]  #stores P(Click) first, will collect the other probs 
  		no_click_probs_list = [float(feature_dict["click_prob"]["0"])] #stores P(No click) first, will collect other no click probs
		for i in range(5,20):
			if words[i] in feature_dict[fields[i-5]]:  #get P(feature_i's category | Click/No Click) into the lists
				click_probs_list.append(float(feature_dict[fields[i-5]][words[i]]["1"]))
				no_click_probs_list.append(float(feature_dict[fields[i-5]][words[i]]["0"]))
			else:
				click_probs_list.append(float(feature_dict[fields[i-5]]["strange"]["1"]))  #put P(feature's strange | Click/No click) into lists
				no_click_probs_list.append(float(feature_dict[fields[i-5]]["strange"]["0"]))
		click_product = reduce(mul, click_probs_list) #P(cat1 | Click)*...*P(cat_k | Click)*P(Click)
		no_click_product = reduce(mul, no_click_probs_list) #P(cat1 | No Click)*...*P(cat_k | No Click)*P(No Click)
		denominator = click_product + no_click_product
		predict_prob = float(click_product)/denominator
		print '%s\t%s\t%s' %  (words[1], "pred", predict_prob)  #outputs <id> \t "pred" \t <predict_prob>
		print '%s\t%s\t%s' %  (words[1], "act", words[2])  #outputs <id? \t "act" \t <1 or 0