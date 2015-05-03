numbers = []

for i in range(2,101):
	for j in range(2,101):
		x = i**j
		if not x in numbers:
			numbers.append(x)

#print(numbers)
print(len(numbers))