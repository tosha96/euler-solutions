import euler

count = 0

for i in range(2,1001):
	if euler.isprime(i):
		circular_prime = True
		for j in range(len(list(str(i)))):
			number = list(str(i))
			chosen_character = number.pop(j)
			new_prime = 0
			if number != []:
				other_characters = number
				new_prime = int(str(chosen_character) + ''.join(other_characters))
			else:
				new_prime = int(str(chosen_character))
			if not euler.isprime(new_prime):
				circular_prime = False
				break
			print(new_prime)
		if circular_prime:
			count += 1
			#print(i)

print("Count: " + str(count))