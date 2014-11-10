feature_new_id = {}
for line in sys.stdin:
	line = line.strip()
	words = line.split('\t')
	if len(words) = 10:
		feature_list = ['appd_id','device_id','user_id',....]
		for tuples in enumerate(feature_list):
			index, feature = tuples[0], tuples[1]
			if feature not in feature_new_id:
				if words[index] not in feature_list[feature].keys():
					feature_new_id[feature][words[index]] = 1
					


