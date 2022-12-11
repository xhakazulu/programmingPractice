name = 'Mary'

print ('What is your name?')
newName = input()

if newName == name:
    print ('Hello Mary')

else:
    print ('Would you like to create an account? (y/n)')

    if input() == 'y' or 'yes':
        print('Creating new account...')
        print('Welcome to the Kooniverse, ' + newName)
    else:
        print ('Go fuck yourself')
