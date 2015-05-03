alphabet = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, 
"q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26, }

f = open('p22in.txt', 'r')

read_data = f.read()
names = read_data
f.close()

names = names.split(',')
for i in range(len(names)):
	names[i] = names[i].replace("\"", "")
	names[i] = names[i].lower()
names.sort()

total = 0

for i in range(len(names)):
	namescore = 0
	for char in names[i]:
		namescore = namescore + alphabet[char]
	namescore = namescore * (i + 1)
	total = total + namescore

print total