#!/usr/bin/python

from operator import mul
import sys
import os.path
sys.path.append(os.path.dirname(__file__))

fields = ["banner_pos", "site_id", "site_domain", "site_category", "app_id","app_domain", 
"app_category", "device_id", "device_ip", "device_os", "device_make", "device_model", 
"device_type", "device_conn_type", "device_geo_country"]

"""def read_probs():
	probs = {}
	# read prob file
    with open("bayes_probs.txt", "r") as f:
    	lines = f.readlines()
    for line in lines:
    	line = line.strip()
        feature, value, prob_click, prob_no_click = line.split('\t')
        key = "%s,%s" % (feature, value)
        probs[key] = (float(prob_click), float(prob_no_click))
    return probs"""

def read_probs():
	probs = {}
	with open("bayes_probs.txt", "r") as f:
		lines = f.readlines()
	for line in lines:
		line = line.strip()
		feature, value, prob_click, prob_no_click = line.split('\t')
		key = "%s,%s" % (feature,value)
		probs[key] = (float(prob_click), float(prob_no_click))
	return probs

prob_dict = read_probs()

for line in sys.stdin:
	line = line.strip()
	words = line.split("\t")
	if len(words) == 28 and words[0] == "validation":
		click_prob_list = [prob_dict["Total,Total"][0]]
		no_click_prob_list = [prob_dict["Total,Total"][1]]
		for i in range(5,20):
			feature = fields[i-5]
			value = words[i]
			key = "%s,%s" % (feature, value)
			if key in prob_dict:
				click_prob_list.append(prob_dict[key][0])
				no_click_prob_list.append(prob_dict[key][1])
			else:
				key = "%s,%s" % (feature, "strange")
				click_prob_list.append(prob_dict[key][0])
				no_click_prob_list.append(prob_dict[key][1])
		click_product = reduce(mul, click_prob_list) #P(cat1 | Click)*...*P(cat_k | Click)*P(Click)
		no_click_product = reduce(mul, no_click_prob_list) #P(cat1 | No Click)*...*P(cat_k | No Click)*P(No Click)
		denominator = click_product + no_click_product
		predict_prob = float(click_product)/denominator
		print '%s\t%s\t%s' %  (words[1], "pred", predict_prob)  #outputs <id> \t "pred" \t <predict_prob>
		print '%s\t%s\t%s' %  (words[1], "act", words[2])


