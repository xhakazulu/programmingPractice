total = 0

for i in range(101):
    total = total + i
    print (str(total-i) + ' plus ' + str(i) + ' equals ' + str (total)) # (total - i) is necessary for display uniformity

print('The sum of all numbers below 100 is ' + str(total))
