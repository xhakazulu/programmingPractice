print ('Enter Spam')

spam = input()

while int(spam) < 10:
    if int(spam) == 1:
        print("Hello")
    elif (spam) == 2:
        print('Howdy')
    else:
        print ('Greetings')
    spam = int(spam) + 1

