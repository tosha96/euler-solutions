def factorial(number):
	if number == 0:
		return 1
	else:
		#print number * factorial(number - 1)
		return number * factorial(number - 1)

final_sum = 0

for i in range(3,1000001):
	factorial_sum = 0
	for c in str(i):
		factorial_sum += factorial(int(c))
	if factorial_sum == i:
		print(i)
		final_sum += i

print("Sum: " + str(final_sum))
