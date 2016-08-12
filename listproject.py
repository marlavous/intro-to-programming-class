master_list = {"Target": ["socks", "soap", "detergent", "sponges"], "Safeway": ["butter", "cake", "cookies", "bread"]}

test_list = ["apples", "wine", "cheese"]

def main_menu():
	print "Select one"
	print "0 - Main Menu"
	print "1 - Show all lists."
	print "2 - Show a specific list."
	print "3 - Add a new shopping list for a specific store."
	print "4 - Add an item to shopping list."
	print "5 - Remove an item from a shopping list."
	print "6 - Remove a list by name."
	print "7 - Exit"
	choice = int(raw_input())
	return choice

def display_lists():
	return master_list

def specific_list():
	specific = raw_input("which store list would you like to see?")
	print master_list[specific]

def new_list():
	store = raw_input("what store is this list for?")
	master_list[store] = []

def delete_list():
	store = raw_input("what store's list do you want to remove?")
	del master_list[store]	

# def alphabetize():
# 	master_list.sort()
# 	return master_list


def add_item():
	# item = item.lower()
	store = raw_input("which store list would you like to add the item to?")
	if store in master_list:
		item = raw_input("What would you like to add?")
		master_list[store].append(item)

	else:
		print "you do not have a list for that store"

def remove_item():
	pass

def check_repeat():
	pass


def main():
	while(True):
		choice = main_menu()

		if choice == 1:
			# alphabetize()
			print display_lists()

		elif choice == 2:
			print specific_list()

		elif choice == 3:
			print new_list()
			#put add_item function here automatically (so they can add items right after creating a store list)

		elif choice == 4:
			add_item()

		elif choice == 5:
			remove_item()

		elif choice == 6:
			delete_list()

		elif choice == 7:
			break

		else:
			return

if __name__ == '__main__':
	main()