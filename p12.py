ndivisors = 0
divisor = 1
trinumber = 1
number = 2
finished = False

while finished == False:
	ndivisors = 0
	divisor = 1
	trinumber = 0
	for i in range(1, number):
		#print i
		trinumber = trinumber + i
	number += 1
	while divisor <= trinumber:
		if trinumber % divisor == 0:
			ndivisors += 1
		if divisor >= 1000 and ndivisors <= 100:
			break
		divisor += 1
	if ndivisors > 500:
		"Final triangle number: " + str(trinumber)
		"Final number of divisors: " + str(ndivisors)
		finished = True
	print "Triangle number: " + str(trinumber)
	print "Number of divisors: " + str(ndivisors)