shoppinglist =["apples", "cheese", "catfood"]


def additem(item):
	if item.lower != shoppinglist:
		shoppinglist.append(item)
		shoppinglist.sort()
		print "%s has been added to your shopping list" % (item)

	else:
		print "%s already on the list" % (item)

	return shoppinglist

def removeitem(item):
	if item.lower == shoppinglist:
		shoppinglist.remove(item)
		shoppinglist.sort()
		print "%s has been removed from your shopping list" % (item)

	else:
		print "%s was never on the list" % (item)


def main():
	print "Lets make a shopping list!"
	print "Would you like to add something?"

	print additem ("bread")
	print additem ("meat")
	print additem ("apples")
	print shoppinglist
	print removeitem ("apples")

	# choice = str(raw_input())

	# if choice == "yes":
	# 	print "What would you like to add?"
	# 	item = str(raw_input())
	# 	return additem(shoppinglist)
	# 	print shoppinglist

	# elif choice == "no":
	# 	print "Would you like to remove something from your shopping list?"
	# 	choice == str(raw_input())

	# 	if choice == "yes":
	# 		print "what would you like to remove?"
	# 		item = str(raw_input())
	# 		return removeitem()
	# 		print shoppinglist

	

if __name__ == '__main__':
	main()