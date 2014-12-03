#!/usr/bin/python

import sys

fields = ["hour", "C1", "banner_pos", "site_id", "site_domain", "site_category", "app_id", "app_domain", "app_category", "device_id", "device_ip", "device_model", "device_type", "device_conn_type", "C14", "C15", "C16", "C17", "C18", "C19", "C20", "C21", "ip_feature", "id_feature"]

for line in sys.stdin:
    line = line.strip()
    values = line.split(',')
    if len(values) == 26 and values[0] != "id":
        click = values[1]  # click or no-click
        features = dict(zip(fields, values[2::]))
        day = features["hour"][-4:-2]
        if day != "29" and day != "30":
            features["hour"] = features["hour"][-2::]  # get hours from date
                
            # combine C15 and C16, ad size
            features["ad_size"] = features["C15"] + "x" + features["C16"]
                
            features.pop("device_id", None)
            features.pop("device_ip", None)
            features.pop("C15", None)
            features.pop("C16", None)
                
            # remove unknown values for features
            if features["site_id"] == "85f751fd":
                features.pop("site_id", None)
            if features["site_domain"] == "c4e18dd6":
                features.pop("site_domain", None)
            if features["site_category"] == "50e219e0":
                features.pop("site_category", None)
            if features["app_id"] == "ecad2386":
                features.pop("app_id", None)
            if features["app_domain"] == "7801e8d9":
                features.pop("app_domain", None)
            if features["app_category"] == "07d7df22":
               features.pop("app_category", None)
                
            # bin ip_feature and id_feature
            ip = int(features["ip_feature"])
            if 1 <= ip <= 10:
                features["ip_feature"] = '1'
            elif 11 <= ip <= 20:
                features["ip_feature"] = '2'
            elif 21 <= ip <= 50:
                features["ip_feature"] = '3'
            elif ip > 50:
                features["ip_feature"] = '4'
                    
            id = int(features["id_feature"])
            if 1 <= id <= 10:
                features["id_feature"] = '1'
            elif 11 <= id <= 26:
                features["id_feature"] = '2'
            elif 27 <= id <= 50:
                features["id_feature"] = '3'
            elif id > 50:
                features["id_feature"] = '4'
                
            for key in features:
                value = click + "." + key + "." + features[key]
                print "%s\t%s" % (value, 1)
            # count total of clicks and no-clicks
            print "%s\t%s" % (click + ".total.total", 1)