def convert_score_to_grade(score):
	if score >= 90:
		return "A"
	elif score >= 80:
		return "B"
	elif score >= 70:
		return "C"
	elif score >= 60:
		return "D" 
	else:
		return "F"
	

def process_file():
	with open("class_grades.txt") as my_file:
		output_list = my_file.readlines()

	return output_list

def main():
	grade_list = process_file()
	
	del grade_list[0]
	del grade_list[1]

	for score in grade_list:
		score_num = int(score.strip())
		letter = convert_score_to_grade(score_num)
		print str(score_num) + " is a " + letter



if __name__ == '__main__':
	main()