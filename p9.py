finished = False

#Formula from:
#http://www.tsm-resources.com/alists/trip.html https://en.wikipedia.org/wiki/Pythagorean_triple
m = 2
n = 1

a = 0
b = 0
c = 0

while finished == False:
	while n < m:
		a = 2*m*n
		b = m**2 - n**2
		c = m**2 + n**2
		if a+b+c == 1000:
			print a*b*c
			finished = True
		n += 1
	m += 1
	n = 1

##old code that took too long to generate triples

# def trytriplet(a,b,c):
# 	if a**2 + b**2 == c**2 and a*b*c != 0:
# 		return True
# 	else:
# 		return False

# while 1 == 1:
# 	#check if number is a square using float division and exponents
# 	if (int(number**(1/2.0)))**2 == number:
# 		a = 1
# 		b = 1
# 		c = int(number**(1/2.0))
# 		while a < number and finished == False:
# 			b = 1
# 			if trytriplet(a,b,c):
# 				finished = True
# 				print "A: " + str(a)
# 				print "B: " + str(b)
# 				print "C: " + str(c)
# 				print a+b+c
# 			while b < number and finished == False:
# 				if trytriplet(a,b,c):
# 					finished = True
# 					print "A: " + str(a)
# 					print "B: " + str(b)
# 					print "C: " + str(c)
# 					print a+b+c
# 				b += 1
# 			a += 1
# 		finished = False
# 	number += 1