import sys

"""Aggregate the conditional probabilities to output the relevant probabilities for 
each feature value."""

for line in sys.stdin:
	line = line.strip()
	words = line.split("\t")
	if len(words) == 5: # line for a feature value
		if words[0] == "0": # no-click
			current_cat = words[2]  # store current feature value
			cond_no_click = words[3]  # probability of feature value cond on no-click
		elif words[0] == "1" and words[2] == current_cat:
			cond_click = words[3]
			print '%s\t%s\t%s\t%s' % (words[1], current_cat, cond_click, cond_no_click)
	elif len(words) == 4: # total probability of either click or no-click
		if words[0] == "1":
			prob_click = words[2]
		elif words[0] == "0":
			prob_no_click = words[2]
			print '%s\t%s\t%s\t%s' % ("Total", "Total", prob_click, prob_no_click)

        