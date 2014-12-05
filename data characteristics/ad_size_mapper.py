#!/usr/bin/python

'''put this mapper in AWS to map all the combinations of colum C15 and C16.
Then using the reducer to aggregate the same combinations to get the final count for all the combinations in the train
'''
import sys

for line in sys.stdin:
	line = line.strip()
	values = line.split(',')
	if len(values) == 24 and values[0] != 'id':
		c15, c16 = values[17], values[18]
		ad_size  = c15 + '.' + c16
		print '%s\t%s' % (ad_size,1)