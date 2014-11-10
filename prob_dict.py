import sys
from operator import mul
 
"""Extract the probability of click in dataset.
"""
list_reuse = []

for line in sys.stdin:
	line = line.strip()
	words = line.split(",")
	if words[0] == "click":
		click_prob = float(words[1])
	list_reuse.append(line)

"""Create a dictionary of dictionaries, where each inner-dictionary
corresponds to a type of feature, and the objects in the
dictionary correspond to click-probabilities for each feature
category."""
feature_dict = {}
for line in list_reuse:
	line = line.strip()
	words = line.split(",")
	if len(words) == 4:
		feature, category, prob = words[0], words[1], words[2]
		if feature not in feature_dict:
			feature_dict[feature] = {}
			feature_dict[feature][category] = prob
		elif feature in feature_dict:
			feature_dict[feature][category] = prob

"""For each line in the validation/test data, create a list of
the relevant probabilities from the dictionary feature_dict,
take products to come up with the numerator for naive Bayes"""
act = []
pred = []

for line in list_reuse:
	line = line.strip()
	words = line.split(",")
	if len(words) == 27:
  		prob_list = [] 
		for i in range(4,19):
			#
			if words[i] in feature_dict[str(i-4)]:
				prob_list.append(float(feature_dict[str(i-4)][words[i]]))
			else:
				prob_list.append(float(feature_dict[str(i-4)]["strange"]))
		numerator = reduce(mul, prob_list)*click_prob
		#equal to P(X1 | Click = 1)*P(X2 | Click = 1)....*P(X_k|Click = 1)*P(Click = 1)
		if numerator > 0.5:
			classify = 1
		else:
			classify = 0
		print '%s\t%s\t%s' % (words[0], numerator, classify)
		#prints id, probability of click, classification of click 
		#act.append(words[1])
		#pred.append(numerator)
		#new lists of actual and predictions for log loss function input