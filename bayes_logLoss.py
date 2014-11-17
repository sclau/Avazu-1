#!/usr/bin/python

"""compute the log-loss value for the predicted instances
"""

import sys
import scipy as sp

def llfun(act, pred):
    epsilon = 1e-15
    pred = sp.maximum(epsilon, pred)
    pred = sp.minimum(1-epsilon, pred)
    ll = sum(act*sp.log(pred) + sp.subtract(1,act)*sp.log(sp.subtract(1,pred)))
    ll = ll * -1.0/len(act)
    return ll

act = []  #to store all the actual 1/0 values
pred = []  #to store all the predicted values ranging from (0,1)

for line in sys.stdin:
	line = line.strip()
	words = line.split("\t")
	if words[1] == "act":
		act.append(float(words[2]))
	elif words[1] == "pred":
		pred.append(float(words[2]))

print llfun(act, pred)

