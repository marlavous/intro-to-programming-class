

def open_file(file_name):
	with open(file_name) as my_file:
		output_list = my_file.read()
	return output_list.split('\n')

def compare_favs(grace, marla):
	for item1 in grace:
		for item2 in marla:
			if item1 == item2:
				return True
	return False
	print grace, marla


def main():
	
	grace = open_file("grace_fav_foods.txt")

	marla = open_file("marla_fav_foods.txt")

	thing = compare_favs(grace, marla)

	if thing == False:
		print "our fav foods are different"

if __name__ == '__main__':
	main()