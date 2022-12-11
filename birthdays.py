birthdays={'Alice':'Apr 1','Bob':'Dec 12', 'Carol':'Mar 4'}

while True:
    name = input('Enter a name (blank to quit): ')
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name],'is the birthday of',name)
    else:
        print('I dont have birthday information for '+ name)
        bday=input('What is their birthday? ')
        birthdays[name]=bday
        if bday=='':
            print('Program terminated')
            break
        print('Birthdays database has been updated')
    break

#Same drill, but using setdefault() Method
        
while True:
    name = input('Enter a name (blank to quit): ')
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name],'is the birthday of',name)
    if name not in birthdays:
        print('I dont have birthday information for '+ name)
        print('What is their birthday?')
        birthdays.setdefault(name,input())
        print('Birthdays database has been updated')
        
