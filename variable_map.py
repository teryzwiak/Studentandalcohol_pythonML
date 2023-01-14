class variable_map:
	def map(students):
		maps = {
			'no': 0,
			'yes': 1
		}
		students['schoolsup'] = students['schoolsup'].apply(lambda x: maps[x])
		students['famsup'] = students['famsup'].apply(lambda x: maps[x])
		students['paid'] = students['paid'].apply(lambda x: maps[x])
		students['activities'] = students['activities'].apply(lambda x: maps[x])
		students['nursery'] = students['nursery'].apply(lambda x: maps[x])
		students['higher'] = students['higher'].apply(lambda x: maps[x])
		students['internet'] = students['internet'].apply(lambda x: maps[x])
		students['romantic'] = students['romantic'].apply(lambda x: maps[x])
		return students

