# 20 x 20 grid
limit = 4
# nested list
matrix = []
greatestproduct = 0

f = open('p11in.txt', 'r')

for line in f:
	splitstring = line.split()
	matrix.append(splitstring)

f.close()

# print int(matrix[0][0]) * int(matrix[0][0 + 1]) * int(matrix[0][0 + 2]) * int(matrix[0][0 + 3])

#do all types of multiplication starting at top left value and ending at bottom right 
for row in range(len(matrix)):
	for value in range(len(matrix[row])):
		if value + 3 <= 19:
			#do horizontal multiplication from left to right
			product = int(matrix[row][value]) * int(matrix[row][value + 1]) * int(matrix[row][value + 2]) * int(matrix[row][value + 3])
			if product > greatestproduct:
				greatestproduct = product
		if row + 3 <= 19:
			#do vertical multiplication from top to bottom
			product = int(matrix[row][value]) * int(matrix[row + 1][value]) * int(matrix[row + 2][value]) * int(matrix[row + 3][value])
			if product > greatestproduct:
				greatestproduct = product
		if value + 3 <= 19 and row + 3 <= 19:
			#do diagonal multiplication from top left to bottom right 
			product = int(matrix[row][value]) * int(matrix[row + 1][value + 1]) * int(matrix[row + 2][value + 2]) * int(matrix[row + 3][value + 3])
			if product > greatestproduct:
				greatestproduct = product
		if value - 3 >= 0 and row + 3 <= 19:
			#do diagonal multiplication from top right to bottom left
			product = int(matrix[row][value]) * int(matrix[row + 1][value - 1]) * int(matrix[row + 2][value - 2]) * int(matrix[row + 3][value - 3])
			if product > greatestproduct:
				greatestproduct = product

print "Greatest product is: " + str(greatestproduct)