fibnums = [1,2,0]
finished = False
counter = 3

while (finished == False):
	fibnums[2] = fibnums[0] + fibnums[1]
	fibnums[0] = fibnums[1]
	fibnums[1] = fibnums[2]
	counter += 1
	if len(str(fibnums[2])) == 1000:
		print fibnums[2]
		print "done"
		print counter
		finished = True