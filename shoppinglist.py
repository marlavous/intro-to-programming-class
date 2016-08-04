shoppinglist =[]

def alphabetize():
	shoppinglist.sort()
	return shoppinglist

def additem(item):
	item = item.lower()
	if item != shoppinglist:
		item.append(shoppinglist)
		print "s% has been added to your shopping list" % (item)

	else:
		print "That is already on the list"

	return shoppinglist

def removeitem(item):
	item = item.lower()
	if item == shoppinglist:
		item.remove(item)
		print "s% has been removed from your shopping list" % (item)

	else:
		print "s% was never on the list" % (item)


def main():
	print "Lets make a shopping list!"
	print "Would you like to add something?"
	choice = str(raw_input())

	if choice == "yes":
		print "What would you like to add?"
		item = str(raw_input())
		return additem(shoppinglist)
		return alphabetize(shoppinglist)
		print shoppinglist

	elif choice == "no":
		print "Would you like to remove something from your shopping list?"
		choice == str(raw_input())

		if choice == "yes":
			print "what would you like to remove?"
			item = str(raw_input())
			return removeitem()
			return alphabetize()
			print shoppinglist



if __name__ == '__main__':
	main()