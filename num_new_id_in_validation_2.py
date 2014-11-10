import sys

feature_new_id = {}
for line in sys.stdin:
	line = line.strip()
	words = line.split(',')
	if len(words) == 27:
		for i in range(4,19):
			if str(i) not in feature_new_id:
				feature_new_id[str(i)] = []
				if words[i] not in feature_list[str(i-4)].keys():
					feature_new_id[str(i)].append(words[i])
			else:
				if words[i] not in feature_list[str(i-4)].keys():
					if words[i] not in feature_new_id[str(i)]:
						feature_new_id[str(i)].append(words[i])


