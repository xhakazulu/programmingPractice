name = ''
nameCount = 0

while name != 'your name':
    print ('Please type your name')
    name = input()
    nameCount = nameCount + 1

    if nameCount == 3:
        print ('Access denied')
        break
        
    


print ('Thank you')
