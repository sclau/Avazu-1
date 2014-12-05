#!/usr/bin/python
'''Put in the AWS after the ad_size_mapper.py
This aggregates the counts for the same ad_size combination
The final output is:
ad_size /t total_count
'''

import sys

current_size = None

for line in sys.stdin:
	line = line.strip()
	ad_size, count = line.split('\t')
	if ad_size == current_size:
		total_count += int(count)
	else:
		if current_size:
			print '%s\t%s' % (current_size, total_count)
		current_size = ad_size
		total_count = int(count)

if ad_size == current_size:
	print '%s\t%s' % (current_size, total_count)