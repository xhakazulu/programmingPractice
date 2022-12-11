# Python program for practical application of sqrt() function
#Checks for prime numbers between 1 and 10000

# import math module
import math

# function to check if prime or not
def check(n):
	if n == 1:
		return False
		
		# from 1 to sqrt(n)
	for x in range(2, (int)(math.sqrt(n))+1):
		if n % x == 0:
			return False
	return True

# driver code
numCount=0
for n in range (1, 10000):
    if check(n):
            print(n)
            numCount=numCount+1
print (str(numCount) + ' results found')

import pyperclip
pyperclip.copy(numCount)
