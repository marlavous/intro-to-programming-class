for i in range(21):
	if i == 13:
		print "hello"
	else:
		print i,


fruits = ["apples", "oranges", "bananas"]
for i in range(len(fruits)):
	print fruits[i]

def sum_nums(num):
	sum = 0
	for i in range(num + 1):
		sum += 1
	return sum

print sum_nums(3)

def sum_num2(num):
	sum = 0 
	if (num < 0):
		for i in range(0, num-1, -1):
			sum += 1

	else :
		for i in range(num + 1):
			sum += 1
	return sum

print sum_num2(-3)


