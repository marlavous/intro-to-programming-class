full_name_tuple = ("first_name", "last_name")
name_list = []

def full_name(full_name_tuple):
	index = len(full_name_tuple) -1
 	for i in range(index, -1, -1):
		name_list.append(full_name_tuple[i])
	print name_list


full_name(full_name_tuple)



for i in range(1000, 0, -100):
	print i
	

names = ["Steven", "Michael", "James"]

for i in range(len(names)):
	print names[i], names[i -1]
	print names[i], names[i -2]

