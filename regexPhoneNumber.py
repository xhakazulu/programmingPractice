import re

message = 'Call me at 072-937-8506 tomorrow, or at 077-658-7014 at my office'


phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchObject=phoneNumRegex.search(message)
print(matchObject.group())


phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print('Found numbers:')
print(phoneNumRegex.findall(message))


