import contacts_manager


def menu_choice():

	print "0 - Main Menu"
	print "1 - Show all contacts"
	print "2 - Add a new contact"
	print "3 - Edit a contact"
	print "4 - Delete a contact"
	print "5 - Exit the program."

	choice = int(raw_input("Choose from the menu options."))

	return choice

def main():
	choice = menu_choice()

	while True:
		if choice == 0:
			choice = menu_choice()
		elif choice == 1:
			show_all_contacts()
			choice = 0
		elif choice == 2:
            item = raw_input("Please enter a new first name to add OR type X if done.")
            if item.upper() == "X":  # return to main menu
                choice = 0
            else:
                print add_shopping_list(item)
        elif choice == 3:
            item = raw_input("Please enter an item to remove OR type X if done.")
            if item.upper() == "X":  # return to main menu
                choice = 0
            else:
                print remove_item(item)
        elif choice == 4:


    	elif choice == 5:
    		break
    	else:
    		print "Try again. Enter a valid choice"
            


first = raw_input("What is the first name?").upper().strip()
last = raw_input("What is the last name?").upper().strip()
mobile = raw_input("What is their cell number?").upper().strip()
email = raw_input("What is their email address?").upper().strip()