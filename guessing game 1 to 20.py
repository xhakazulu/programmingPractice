import random

print ('I am thinking of a number between 1 and 20. ')

randnum = random.randint(1,20)

for guesses in range(1,7):
    print ('Take a guess\nYou have '+ str(6-guesses) + ' chances')
    guess = int (input())
    
    if guess < randnum:
        print('Your guess is too low')
    elif guess > randnum:
        print('Your guess is too high')
    else:
        break #This condition is the correct guess

if guess == randnum:
    print('Good job! \nYou guessed my number in ' + str(guesses) + ' guesses')


else:
    print('Sorry, the number I was thinking of was ' + str (randnum))
