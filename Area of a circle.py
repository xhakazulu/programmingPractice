# Accepts the radius of a circle from the user and compute the area

print ('What is the radius (r) of your circle in cm?')
radius = input ()

# Area (A) = pi * r^2
pi = 3.14159265359
print ('For \t Area (A) = pi * r^2: \nAnd pi = 3.14159265359 \n Therefore')

print ('The area (A) of your circle is ' + str (float (radius)**2 * pi) + ' cm2')
