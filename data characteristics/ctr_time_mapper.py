#!/usr/bin/python
''' Put in AWS EMR or local machine to see the 24 hours' CTR, regardless of day
If execute this locally, the command is:
python ctr_time_mapper.py < train > time_map_out.txt
sort time_map_out.txt > time_red_in.txt
python ctr_time_reducer.py < time_red_in.txt > time_red_out.txt
'''
import sys

for line in sys.stdin:
	line = line.strip()
	values = line.split(',')
	if len(values) == 24 and values[0] != 'id':
		time = values[2][-2:]
		click = values[1]
		print '%s\t%s' % (time, click)