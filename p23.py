def sumofpd(number):
	sum = 0
	for divisor in range(1, number + 1):
		if number % divisor == 0 and number != divisor:
			sum = sum + divisor
	return sum

abundants = []
cantbesummedsum = 0

#generate list of abundants less than number which all integers greater than it can be created by the sum of abundant number
for number in range(1, 28125):
	if sumofpd(number) > number:
		abundants.append(number)
		print number

print abundants

for number in range(1, 28124):
	print number
	canbesummed = False
	for abundant in abundants:
		if abundant < number:
			result = number - abundant
			if result in abundants:
				canbesummed = True
				break
	if not canbesummed:
		cantbesummedsum = cantbesummedsum + number

print "Sum: " + str(cantbesummedsum)

