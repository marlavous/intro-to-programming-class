def tip(bill, percent):
	return bill * percent * .01

def check (bill, tip):
	return bill + tip

def divide (check, covers):
	return check / covers

def main():
	print "choose one"
	print "1 - calculate tip"
	print "2 - split the bill"
	choice = int(raw_input())

	if choice == 1:
		bill = float(raw_input("How much was the bill?"))
		percent = float(raw_input("What percent gratuity do you want to leave?"))
		gratuity = tip(bill, percent)
		total_bill = check(bill, tip)
		print "The tip is %f." % tip
		print " The bill total is %f." % total_bill
		split_check = raw_input("Would you like to split the bill, yes or no?")
		if split_check == "yes":
			covers = raw_input("How many ways would you like the bill split?")
			perperson = divide(check, covers)
			print "The bill is %f each." % divide

	elif choice ==2:
		bill = float(raw_input("How much was the bill?"))
		covers = float(raw_input("How man ways would you like the bill split?))
		perperson = divide(bill,covers)
		print "the bill is %f each." % divide


if __name__ == '__main__':
	main()
