class Contact(object):
	def __init__(self, name, surname, mobile="", email=""):
		self.name = name
		self.surname = surname
		self.mobile = mobile
		self.email = email

	def send_text(self,message):
		if self.mobile != "":
			print "to:%s - %s - %s" % (self.name, self.mobile, message)
		else:
			print self.name + ":no mobile number available"

	def send_email(self, message):
		if send_email != "":
			print "to: %s - %s" % (self.email, message)
		else:
			print "No email available"

def main():

	contacts = []

	contact_jenny = Contact("Jenny", "Jones", mobile="415-867-5309", email="jenny@me.com")
	contact_fitz = Contact("FitzChivalry", "Farseeer",)
	contact_dar = Contact("D'Artagnan", "Marcianelli", mobile="415-826-7090",)
	contact_cate = Contact("Cate", "Mason", email="catepult@sbcglobal.net")

	
	contacts.append(contact_cate)
	contacts.append(contact_dar)
	contacts.append(contact_fitz)
	contacts.append(contact_jenny)

	for info in contacts:
		print info.name, info.surname, info.mobile, info.email

	for info in contacts:
		info.send_text("Hey girl, hey"),




if __name__ == '__main__':
	main()