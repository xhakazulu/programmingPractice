#Test source: https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

number = int(input("Enter a number: "))

if number%2 == 1:
    print (str(number) + " is an odd number")
else:
    print (str(number) + " is an even number")

#Extras #1:
if number%4 == 0:
    print(str(number) + ' also happens to be a multiple of 4.')


#Extras #2:

num = int(input("Enter a number (num): "))
check = int(input("Enter another number(check): "))

if num%check == 0:
    print(str(check) + ' is a multiple of ' + str(num))

else:
    print (str(check) + ' is not a multiple of ' + str(num))
