#!/usr/bin/python

import sys

for line in sys.stdin:
	line = line.strip()
	words = line.split(",")
	if len(words) == 24 and words[0] != "id":
		device_id, device_ip = words[11], words[12]
		time = words[2]
		id = words[0]
		day = time[4:6]  #removes the hour from time
		print "%s.%s\t%s\t%s" % (day, device_id, device_ip, id)