#!/usr/bin/python

import sys

current_day = "Start"
current_id = "Start"
current_ip = "Start"

ip_count = "Start"
id_count = "Start"

for line in sys.stdin:
	line = line.strip()
	words = line.split("\t")
	if len(words) == 3:
		day, device_id = words[0].split(".")
		device_ip = words[1]
		id = words[2]

		if day == current_day:
			if device_id == current_id:
				if device_ip == current_ip:
					id_count += 1
				elif device_ip != current_ip:
					id_count += 1
					ip_count += 1
					current_ip = device_ip
			elif device_id != current_id:
				print "%s\t%s\t%s\t%s" % (current_day, current_id, ip_count, id_count)
				current_id = device_id
				current_ip = device_ip
				id_count = 1
				ip_count = 1
		elif day != current_day and current_day != "Start":
			print "%s\t%s\t%s\t%s" % (current_day, current_id, ip_count, id_count)
			current_day = day
			current_id = device_id
			current_ip = device_ip
			id_count = 1
			ip_count = 1
		elif day != current_day and current_day == "Start":
			current_day = day
			current_id = device_id
			current_ip = device_ip
			id_count = 1
			ip_count = 1

print "%s\t%s\t%s\t%s" % (current_day, current_id, ip_count, id_count)