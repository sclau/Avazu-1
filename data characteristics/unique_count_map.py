#!/usr/bin/python

'''First aggreate the test and the train to one file
Then run the mapper and redcuer to get the number of unique features in both train and test
and finally see for these features, what's the percentage of overlap
'''

import sys
train_col = ['ID', 'click', 'hour', 'C1', 'banner_pos', 'site_id', 'site_dom',\
			'site_cat', 'app_id', 'app_dom', 'app_cat', 'device_id',\
			'device_ip', 'device_model', 'device_type', 'device_conn_type',\
			'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20', 'C21']

test_col = ['ID', 'hour', 'C1', 'banner_pos', 'site_id', 'site_dom',\
			'site_cat', 'app_id', 'app_dom', 'app_cat', 'device_id',\
			'device_ip', 'device_model', 'device_type', 'device_conn_type',\
			'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20', 'C21']

for line in sys.stdin:
	line = line.strip()
	values = line.split(',')
	if len(values) == 24:
		if values[0] != 'id':
			for i in range(0,24):
				col_value = train_col[i] + '.' + values[i] 
				print '%s\t%s\t%s' % (col_value,1,'train')

	if len(values) == 23:
		if values[0] != 'id':
			for i in range(0,23):
				col_value = test_col[i] + '.' + values[i] 
				print '%s\t%s\t%s' % (col_value,1,'test')

		