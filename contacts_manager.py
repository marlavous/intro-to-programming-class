import contact

def main():

	contactlist = []
	print "Add a new contact"

	new = contact.Contact(name=first, surname=last, mobile=mobile, email=email)

	first = raw_input("What is the first name?")
	last = raw_input("What is the last name?")
	mobile = raw_input("What is their cell number?")
	email = raw_input("What is their email address?")

	contactlist.append(new)

	for info in contactlist:
		print info.name, info.last, info.mobile, info.email


if __name__ == '__main__':
	main()