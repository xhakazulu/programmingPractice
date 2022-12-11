#program that counts the instance of each letter in the user-generated phrase

import pprint

message=input('Enter a statement: ')
count={}

for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1

pprint.pprint(count)

'''
If you want to obtain the prettified text as a
string value instead of displaying it on the
screen, call pprint.pformat() instead.
'''
