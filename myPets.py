myPets = ['Zophie','Pooka','Fat-tail']
print('Enter a pet name')
name = input()
if name not in myPets:
    print('I do not have a pet named',name)
    print ('Do you want to add', name,'to your pets? Y/N')
    newCatResponse = input()
    if newCatResponse == 'Y' or 'y':
        myPets = myPets + [name]
        print (name,'has been added to pets')
else:
    print(name,'is my pet')
