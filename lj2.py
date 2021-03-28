import math
pi = math.pi
def print_volume(r):
    return 4 /3*pi*(r**3)
print(print_volume(2)) #output 33.5103216
print(print_volume(3)) #output 113.097335
print(print_volume(4)) #output 268.082573

import math
pi = math.pi
def circleCircumf(r):
    return 2*pi*r
#Doubles the circumference of a circle
def doubleCircumf(x):
    return 2 * circleCircumf(x)
print(doubleCircumf(2)) #25.132741
print(doubleCircumf(2.5)) #31.41592
print(doubleCircumf(3)) #37.699111
#Demonstrates math module and nested functions