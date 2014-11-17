import sys
import json

"""feature_dict looks like 
{feat1:{cat1:{1:prob click, 0:prob not click}, cat2:{1:prob click, 0:prob not click}}, 
feat2:{cat1:{1:prob click, 0:prob no click}}, so on for other features}
"click_prob":{1: P(Click), 0:P(No Click)}}"""

feature_dict = {}
for line in sys.stdin:
	line = line.strip()
	words = line.split("\t")
	if len(words) == 5:
		click_or_not, feature, category, prob = int(words[0]), words[1], words[2], float(words[3])
		if feature not in feature_dict:
			feature_dict[feature] = {}
			feature_dict[feature][category] = {1:0, 0:0} #set the probabilities to 0 for both click/not for now
			feature_dict[feature][category][click_or_not] = prob
		elif feature in feature_dict:
			if category not in feature_dict[feature]:
				feature_dict[feature][category] = {1:0, 0:0}
				feature_dict[feature][category][click_or_not] = prob #if cat not alrdy inside, then fill one of the probs and leave the other as 0
			elif category in feature_dict[feature]:
				feature_dict[feature][category][click_or_not] = prob #if category alrdy inside, then filling in the other probability
	elif len(words) == 4:  #creates click_prob: {1: P(click), 0: P(No Click)}
		click_or_not, prob = int(words[0]), float(words[2])
		if "click_prob" not in feature_dict:
			feature_dict["click_prob"] = {}
			feature_dict["click_prob"][click_or_not] = prob
		elif "click_prob" in feature_dict:
			feature_dict["click_prob"][click_or_not] = prob 

with open('dict.json', 'wb') as fp:
    json.dump(feature_dict, fp)