numbers = []
bigsum = 0

f = open('p13in.txt', 'r')

for line in f:
	numbers.append(int(line))

f.close()

for i in numbers:
	bigsum = bigsum + i

print bigsum