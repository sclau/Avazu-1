#!/usr/bin/python
'''First aggreate the test and the train to one file
Then run the mapper and redcuer to get the number of unique features in both train and test
and finally see for these features, what's the percentage of overlap
'''

import sys
current_doc = None
current_col_value = None
unique_train = 0 
unique_test = 0

for line in sys.stdin:
	line = line.strip()
	col_value, count, doc = line.split('\t')
	if col_value == current_col_value:
		if doc != current_doc:
			if doc == 'train':
				num_overlap += 1
				unique_train += 1
				current_doc = doc
			else:
				num_overlap += 1
				unique_test += 1
				current_doc = doc
		else:
			continue

	else:
		if current_col_value is not None:
			if col_value.split('.')[0] == current_col_value.split('.')[0]:
				if doc == 'train':
					unique_train += 1
					current_doc = doc
					current_col_value = col_value
				else:
					unique_test += 1
					current_doc = doc
					current_col_value = col_value
			else:
				col = current_col_value.split('.')[0]
				print '%s\t%s\t%s\t%s' % (col,unique_train,unique_test,num_overlap)

				current_col_value = col_value
				unique_test = 1
				unique_train = 1
				num_overlap = 0
		else:
				current_col_value = col_value
				unique_test = 1
				unique_train = 1
				num_overlap = 0

if col_value == current_col_value:
	if doc == current_doc:
		col = current_col_value.split('.')[0]
		print '%s\t%s\t%s\t%s' % (col,unique_train,unique_test,num_overlap)
	elif doc != current_doc:
		col = current_col_value.split('.')[0]
		if doc == 'train':
			unique_train += 1
			num_overlap += 1
		else:
			unique_test += 1
			num_overlap += 1
		print '%s\t%s\t%s\t%s' % (col,unique_train,unique_test,num_overlap)
elif col_value != current_col_value and col_value.split('.')[0] == current_col_value.split('.')[0]:
	if doc == 'train':
		unique_train += 1
	else:
		unique_test += 1
	col = current_col_value.split('.')[0]
	print '%s\t%s\t%s\t%s' % (col,unique_train,unique_test,num_overlap)





