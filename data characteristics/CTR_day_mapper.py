#!/usr/bin/python
''' Put in AWS EMR or local machine to see the CTR for all the days
If execute this locally, the command is:
python CTR_day_mapper.py < train > CTR_day_map_out.txt
sort CTR_day_map_out.txt > CTR_day_red_in.txt
python CTR_day_reducer.py < CTR_day_red_in.txt > CTR_day_red_out.txt
'''
import sys

for line in sys.stdin:
	line = line.strip()
	values = line.split(',')
	if len(values) == 24 and values[0] != 'id':
		day = values[2][4:6]
		click = values[1]
		print '%s\t%s' % (day, click)