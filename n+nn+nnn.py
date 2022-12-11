# Python program that accepts an integer (n) and computes the value of n+nn+nnn

print ('Enter a value, n')
n = input()

product = int(n) + int (n) * int (n) + int(n)*int(n)*int(n)

print ('n + nn + nnn = ' + str(product))
