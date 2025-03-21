#math python library

import math

#exponents

#powe function

print(math.pow(2, 3))
#2 is the base
#3 is the power

#eponential and logarithm
print("Exponenrital of 2:", math.exp(2))
# e^2

print("natural lof of 10:", math.log(10))
#log(10) oe ln(10)
#log base is e, e 2.8

print("log base 10 of 100", math.log(100))
#log10(100)

#Absolut value
print("absolut value og -5:", math.fabs(-5))

#factorial
print("factorial of 5:",  math.factorial(5))

#convert radians to degrees

angle = 45
radians = math.radians(angle)
print(radians)

#whenever you want to use trigonometric function
#you have to convert the angle to radians
#sin to cos

print("sin of 45 degrees:", math.sin(radians))

print("cos of 45 degrees:", math.cos(radians))

print("tan of 45 degrees:", math.tan(radians))

#invers trigo

print("arcsin of 0.5:", (math.asin(0.7071067811865476)))

#this tells me for what angle (radians)
#this will give us

#convert degrees to radians

angle = 60
radians = math.radians(angle)
print(radians)

#calculate sin 60, tan ,cos
      
print("sin of 60 degrees:", math.sin(radians))

print("cos of 60 degrees:", math.cos(radians))

print("tan of 60 degrees:", math.tan(radians))

#take the values of sin 60, cos 60, tan 60
#and use the invers trigonometric functions
#to find the angle in degrees

print("arcsin of 60 degrees:", (math.asin(0.8660254037844386)))
print("arccos of 60 degrees:", (math.acos(0.5000000000000001)))
print("arctan of 60 degrees:", (math.atan(1.7320508075688767)))

print("60 degrees to angle:", (math.degrees(math.atan(1.7320508075688767))))
print("60 degrees to angle:", (math.degrees(math.acos(0.5000000000000001))))
print("60 degrees to angle:", (math.degrees(math.asin(0.8660254037844386))))

#mathematical
print("value of pi:", math.pi)
print("value of e:", math.e)
print("value of tau:", math.tau) # tau = 2 *pi
print("infinity", math.inf)
print("not-a-number (NAN)", math.nan)