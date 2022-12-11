#Test source: https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

print ('What is your name?')
uName=input()

print ('How old are you, ' + uName + '?')
age=int(input())

#calculate birth year
birthYear=2022-age
century=birthYear+100

print('You will turn 100 years in ' + str(century))


#Part 2 of the test
n = int(input("Enter another number: "))

for x in range (n):
    print('You will turn 100 years in ' + str(century)) 

