def sumofpd(number):
	sum = 0
	for divisor in range(1, number + 1):
		if number % divisor == 0 and number != divisor:
			sum = sum + divisor
	return sum

sumofnum = 0

for number in range(1, 10001):
	if sumofpd(sumofpd(number)) == number and number != sumofpd(number):
		print "Number is amicable: " + str(number) + " and " + str(sumofpd(number))
		sumofnum = sumofnum + number

print "Sum of num: " + str(sumofnum)