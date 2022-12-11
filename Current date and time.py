import datetime
now = datetime.datetime.now(tz=None)
print ('Current date and time: ')
print (now.strftime('%d-%m-%Y %H:%M:%S'))
