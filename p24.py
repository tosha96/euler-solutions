def factorial(number):
	if number == 0:
		return 1
	else:
		#print number * factorial(number - 1)
		return number * factorial(number - 1)

def heap(n, elements, perms):
	if n == 1:
		string = ""
		for number in elements:
			string += str(number)
		perms.append(string)
		return elements
	else:
		for i in range(n):
			j = 0
			heap(n - 1, elements, perms)
			if n % 2 == 0:
				elements[i], elements[n - 1] = elements[n - 1], elements[i]
			else:
				elements[0], elements[n - 1] = elements[n - 1], elements[0]


nums = [0,1,2,3,4,5,6,7,8,9]
# nums = [0,1,2]
perms = []

heap(10,nums,perms)

perms.sort()

print perms[999999]