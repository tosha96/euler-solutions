largestchain = 0
number = 1
startingnumber = 0

while number < 1000000:
	chain = 0
	tempnumber = number
	while tempnumber != 1:
		if tempnumber % 2 == 0:
			tempnumber = tempnumber / 2
			#print tempnumber
			chain += 1
		else:
			tempnumber = (3 * tempnumber) + 1
			#print tempnumber
			chain += 1
	chain += 1
	if chain > largestchain:
		largestchain = chain
		startingnumber = number
	print "Starting Number: " + str(number)
	print "Chain Length: " + str(chain)
	number += 1

print "Largest Chain: " + str(largestchain)
print "Best Starting Number: " + str(startingnumber)