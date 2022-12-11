#This program accepts a number from a user and calculate the sum of all numbers from 1 to a given number
#TEST SOURCE: https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/#h-exercise-2-print-the-following-pattern


userNum= int (input (print ("Enter a number: ")))
s=0

for i in range (1, userNum+1):
    s=s+i

print ("The sum of all numbers between 1 and", userNum, "is: " + str(s))
    
