print('Text character to Unicode code point converter'.center(60,'~'))

numericValues={}

for i in range (32,141):
    numericValues[i]=chr(i)
    print (str(i).ljust(9,'`'),chr(i))

for k, v in numericValues:
    print(str(k), v)
    
    print (str(i).ljust(9,'`'),chr(i))
