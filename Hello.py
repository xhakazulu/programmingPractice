# This program says hello and asks for my name

print ('Hello world!')

print ('What is  your name?') # ask for their name
myName = input ()
print ('it is good to meet you, ' + myName)
print ('The length of your name is: ')
print (len(myName))

print('What is your age?') #ask for their age
myAge = int (input())
print('You will be ' + str(myAge + 1)  + ' in a year.')

print('Hey ' + myName + ', who is your girlfriend?')
myGF = input()

print('And what is her age?')
gfAge = input()

ageDiff = int (myAge) - int(gfAge) #calculates age difference

print (myName + ' and ' + myGF + ' are ' + str (ageDiff) + ' years apart.')
print ('You will both be ' + str(int(myAge) + 1) + ' and ' + str (int (gfAge) + 1) + ' years old respectively at the end of this year')

