power_sum = 0
for i in range(1,1001):
	power_sum += i**i
sumstring = str(power_sum)
sumstring = sumstring[-10:]
print(sumstring)