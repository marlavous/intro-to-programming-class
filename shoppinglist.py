shoppinglist = ["apples", "cheese", "catfood"]


def additem(item):
	item = item.lower()
	if item != shoppinglist:
		shoppinglist.append(item)
		shoppinglist.sort()
		print "%s has been added to your shopping list" % (item)

	else:
		print "%s already on the list" % (item)

	return shoppinglist

def removeitem(item):
	item = item.lower()
	if item == shoppinglist:
		shoppinglist.remove(item)
		shoppinglist.sort()
		print "%s has been removed from your shopping list" % (item)

	else:
		print "%s was never on the list" % (item)

def menu():
	print "0 - Main Menu"
	print "1 - Show current list."
	print "2 - Add an item to your shopping list."
	print "3 - Remove an item from your shopping list."
	print "4 - To exit the program."
	choice = raw_input("Choose an option")
	return choice

def main():
	choice = menu()

	while True:
		if choice == 0:
			choice = menu()

		elif choice == 1:
			print shoppinglist.sort()

		elif choice == 2:
			item = raw_input("Enter the item you want to add")
			print additem(shoppinglist)

		elif choice == 3:
			item == raw_input("Which item would you like to remove?")
			print removeitem(shoppinglist)

		elif choice == 4:
			break

if __name__ == '__main__':
	main()