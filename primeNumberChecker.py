# Python program for practical application of sqrt() function

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
while True:
    print('Enter a number')
    n = int(input())
    if check(n):
            print("prime")
    else:
            print("not prime")
