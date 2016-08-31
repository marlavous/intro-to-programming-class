import contact

contactlist = [contact.Contact('michelle', "choi")]

def add_new_contact(first, last, mobile="", email=""):
	new = contact.Contact(name=first, surname=last, mobile=mobile, email=email)
	contactlist.append(new)

def edit_contact(first, last, mobile="", email=""):
	contact = find_contact(first)
	delete_contact(contact)
	add_new_contact(first, last, mobile, email)

# def edit_contact(first, last, mobile="", email=""):
# 	contact = find_contact(first)
# 	contact.first = first
# 	contact.last = last
# 	contact.mobile = mobile
# 	contact.email = email
	
# def edit_contact(contact, part, value):
# 	if part == 'first':
# 		contact.first = value
# 	else if part == 'last':
# 		contact.last = value
# 	...

def delete_contact(contact):
	if contact in contactlist:
		contactlist.remove(contact)
		

def current_contacts():
	for person in contactlist:
		print "%s - %s" % (person.name, person.surname)

def find_contact(name):
	for contact in contactlist:
		if name == contact.name:
			return contact
	return None



def main():

	first = "Michelle" 
	last = "Choi"
	mobile = 5106790093
	email = "mcmiji@gmail.com"

	add_new_contact("marla", "mason", mobile=4565465465, email="marla@me.com")
	print contactlist

	contact = find_contact(first)
	
	edit_contact("Mary", "Smith")

	# contactlist[0].name = "markis"
	# print contactlist[0]

	delete_contact(contact)
	# for person in contactlist:
	#  	print person.__dict__

	current_contacts()



if __name__ == '__main__':
	main()