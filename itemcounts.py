file = 'rittenhouse_data.txt'
f = open(file, 'r')
lines = f.readlines()


def analyze_item_data():
	# Separate dict for group type:  male [M], female [F], child [C], YA [Y], 
	# adult [A], middle-aged [M], Senior [S], Group [G], Single [I]
	counts = {'Male': {},
				'Female': {},
				'C': {},
				'Y': {},
				'A': {},
				'M': {},
				'S': {},
				'G': {},
				'I': {}}

	types = {}
	for i in range(1,22):
		types[i] = {}

	i = 0
	for entry in lines:
		labels, items = entry.rstrip().split('-')
		gender = labels[0]
		age = labels[1]

		# Error checking
		if gender not in ['F', 'M']:
			print 'Gender error at line ' + str(i)
		if age not in ['C','Y','A','M','S']:
			print 'Age error at line ' + str(i)

		if gender == 'M':
			gender = 'Male'
		else:
			gender = 'Female'

		status = 'I'
		if len(labels) ==3:
			status = labels[2]
		elif len(labels) != 2:
			# Sanity check
			print 'Error: incorrect labels in line ' + str(i)
			break

		# See how many items this person was carrying	
		items = items.split(',')
		num = len(items)
		# 11 means they were carrying 'Nothing'!
		if num == 1 and int(items[0]) == 11:
			num = 0

		# Increment counts 
		counts[gender][num] = counts[gender].get(num, 0) + 1
		counts[age][num] = counts[age].get(num, 0) + 1
		counts[status][num] = counts[status].get(num, 0) + 1

		# Go through each item
		for item_num in range(len(items)):
			item_type = int(items[item_num])
			types[item_type][gender] = types[item_type].get(gender, 0) + 1
			types[item_type][age] = types[item_type].get(age, 0) + 1
			types[item_type][status] = types[item_type].get(status, 0) + 1

		i = i + 1

	return counts, types


