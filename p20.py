def factorial(number):
	if number == 0:
		return 1
	else:
		#print number * factorial(number - 1)
		return number * factorial(number - 1)

number = str(factorial(100))
sum = 0

print number

for char in number:
	sum = sum + int(char)

print sum