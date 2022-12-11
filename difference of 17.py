# Write a Python program to get the difference between a given number and 17,
# if the number is greater than 17 return double the absolute difference.

print ('Enter a number')

number = input ()
difference = int (number)- 17

print ('The difference between ' + number + ' and 17 is ' + str(difference))

if abs(difference) > 17:
    difference = abs( difference * 2)
    print ('Since the difference is greater than 17, here is the double of its absolute: ' + str (difference))
