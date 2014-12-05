#!/usr/bin/python

''' Put in AWS EMR or local machine to see the CTR for all the days
If execute this locally, the command is:
python CTR_day_mapper.py < train > CTR_day_map_out.txt
sort CTR_day_map_out.txt > CTR_day_red_in.txt
python CTR_day_reducer.py < CTR_day_red_in.txt > CTR_day_red_out.txt
'''

import sys
current_day = None


for line in sys.stdin:
	line = line.strip()
	day, click = line.split('\t')
	if day == current_day:
		total_click += float(click)
		total_count += 1
	else:
		if current_day:
			CTR = round(total_click/total_count,2)
			print '%s\t%s\t%s\t%s' % (current_day, total_click,total_count,CTR)
		current_day = day
		total_click = float(click)
		total_count = 1

if day == current_day:
	CTR = round(total_click/total_count,2)
	print '%s\t%s\t%s\t%s' % (current_day, total_click,total_count,CTR)
