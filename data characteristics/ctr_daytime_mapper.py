#!/usr/bin/python

''' Put in AWS EMR or local machine to see the 24 hours' CTR, for each day
If execute this locally, the command is:
python ctr_daytime_mapper.py < train > daytime_map_out.txt
sort daytime_map_out.txt > daytime_red_in.txt
python ctr_daytime_reducer.py < daytime_red_in.txt > daytime_red_out.txt
'''
import sys

for line in sys.stdin:
	line = line.strip()
	values = line.split(',')
	if len(values) == 24 and values[0] != 'id':
		daytime = values[2][4:]
		click = values[1]
		print '%s\t%s' % (daytime, click)