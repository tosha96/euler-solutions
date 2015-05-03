sum = 1
bigsum = 1
size = 1
addition = 2

#generates the numbers by adding multiples of 2, and then adds the generated number to the final sum
while size != 1001:
	for i in range(4):
		sum = sum + addition
		bigsum += sum
		print sum
	size = size + 2
	addition = addition + 2

print bigsum