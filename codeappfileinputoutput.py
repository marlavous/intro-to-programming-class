string="food:hotdog,price:5.50"
def total_menu(string):
	food={}
	# for item in menu_list:
	item_parts = string.split(",")
	price_part=item_parts[1].split(":")
	print price_part







def main():
	menu_list = ["food:hotdog,price:5.50","food:burger,price:9.50","food:fries,price:4.00","food:shake,price:5.00"]

	print total_menu(string)

if __name__ == '__main__':
	main()