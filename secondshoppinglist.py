shoppinglist = []

def additem(item):
	item = item.lower()
	if item not in shoppinglist:
		shoppinglist.append(item)
		print "%s has been added to your list" % (item)
	else: 
		print "%s is already on the list" % (item)
	return alphabetizedlist()

def removeitem(item):
	item = item.lower()
	if item in shoppinglist:
		shoppinglist.remove(item)
		print "%s has been removed from your list"
	else:
		print "%s was not on the list."
	return alphabetizedlist()

def alphabetizedlist():
	shoppinglist.sort()
	return shoppinglist

def menuoptions():
	print "0 - Main Menu"
	print "1 - show current list"
	print "2 - add items to list"
	print "3 - remove items from list"
	print "4 - exit the program"
	choice = int(raw_input("choose one"))
	return choice


def main():
	choice = menuoptions()

	while True:
		if choice == 0:
			choice = menuoptions()

		elif choice == 1:
			print alphabetizedlist
			choice = 0 #this is to return to the main menu

		elif choice == 2:
			item = str(raw_input("enter the item to add to your list OR type X if done."))
			if item.upper() == "X":
				choice = 0
			else:
				print additem(item)

		elif choice == 3:
			item = str(raw_input("enter the item you want to remove OR type X if done."))
			if item.upper() == "X":
				choice = 0
			else:
				print removeitem(item)

		elif choice == 4:
			break

		choice = menuoptions()




if __name__ == '__main__':
	main()

