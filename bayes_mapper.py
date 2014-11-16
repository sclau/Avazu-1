#!/usr/bin/python
# python bayes_mapper.py < split2_small_train.txt > counts_small_train.txt

import sys

fields = ["banner_pos", "site_id", "site_domain", "site_category", "app_id","app_domain", "app_category", "device_id", "device_ip", "device_os", "device_make", "device_model", "device_type", "device_conn_type", "device_geo_country"]

for line in sys.stdin:
    line = line.strip()
    values = line.split('\t')
    if len(values) == 28:
        if values[0] == "train":
            click = values[2]  # click or no-click
            features = values[5:20]
            for i in range(0, len(features)):
                key = click + "." + fields[i] + "." + features[i]
                print "%s\t%s" % (key, 1)
            # count total of clicks and no-clicks
            print "%s\t%s" % (click + ".total.total", 1)