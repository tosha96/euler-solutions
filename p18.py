import random

paths = []
failedtries = 0

matrix = []
greatestsum = 0

f = open('p18in.txt', 'r')

for line in f:
	splitstring = line.split()
	matrix.append(splitstring)

f.close()

print range(len(matrix))

while failedtries < 10000:
	sum = 75
	path = []
	position = 0
	for row in range(len(matrix)):
		if row != 14:
			#print row
			if matrix[row][0] == 75:
				print "test"
				sum = sum + int(matrix[row][0])
			else:
				rdirection = random.choice(["left", "right"])
				if rdirection == "left":
					sum = sum + int(matrix[row + 1][position])
					path.append(rdirection)
				elif rdirection == "right":
					sum = sum + int(matrix[row + 1][position + 1])
					position += 1
					path.append(rdirection)
	if not path in paths:
		paths.append(path)
		failedtries = 0
		print sum
		if sum > greatestsum:
			greatestsum = sum
	else:
		failedtries += 1

print greatestsum
#print paths