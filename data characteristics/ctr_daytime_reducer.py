#!/usr/bin/python

''' Put in AWS EMR or local machine to see the 24 hours' CTR, for each day
If execute this locally, the command is:
python ctr_daytime_mapper.py < train > daytime_map_out.txt
sort daytime_map_out.txt > daytime_red_in.txt
python ctr_daytime_reducer.py < daytime_red_in.txt > daytime_red_out.txt
'''

import sys
current_daytime = None

for line in sys.stdin:
	line = line.strip()
	daytime, click = line.split('\t')
	if daytime == current_daytime:
		total_click += float(click)
		total_count += 1
	else:
		if current_daytime:
			print '%s\t%s\t%s' % (current_daytime, total_click,total_count)
		current_daytime = daytime
		total_click = float(click)
		total_count = 1

if daytime == current_daytime:
	print '%s\t%s\t%s' % (current_daytime, total_click,total_count)
