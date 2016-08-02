def eat():
	print "Eat it"

def main():
	print "Should you eat that bacon?"
	print "Do you want to feel like angels are frolicking on your tastebuds?"
	choice = str(raw_input())

	if choice == "yes":
		print eat 

	elif choice == "no":
		print "You've clearly never tasted bacon"
		print eat

	elif choice == "yes, but I'm afraid bacon will kill me":
		print "are you a coward?"

		if choice == "yes":
			print "bacon will turn you into a true warrior"

		elif choice == "I am not!":
			print "then" + eat



if __name__ == '__main__':
	main()