#!/usr/bin/python

''' Put in AWS EMR or local machine to see the 24 hours' CTR, regardless of day
If execute this locally, the command is:
python ctr_time_mapper.py < train > time_map_out.txt
sort time_map_out.txt > time_red_in.txt
python ctr_time_reducer.py < time_red_in.txt > time_red_out.txt
'''

import sys
current_time = None

for line in sys.stdin:
	line = line.strip()
	time, click = line.split('\t')
	if time == current_time:
		total_click += float(click)
		total_count += 1
	else:
		if current_time:
			print '%s\t%s\t%s' % (current_time, total_click,total_count)
		current_time = time
		total_click = float(click)
		total_count = 1


if time == current_time:
	print '%s\t%s\t%s' % (current_time, total_click,total_count)