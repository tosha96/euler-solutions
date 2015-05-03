mul=lambda x,y:x*y
from fractions import Fraction

def nCk(n,k): 
	return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )

print nCk(120,15)

