###An Introduction to Interactive Programming in Python (Part 1) 
##Week 1
#Functions, logic, and operations.

#Funtion that computes the area of a triangle
def triangle_area(base, height):
    area = (1.0/2)*base*height
    return area

a1 = triangle_area(3,8)
print a1
a2 = triangle_area(14,2)
print a2

# convert fahrenheit to celcius
def fahrenheit2celcius(fahrenheit):
    celcius = (5.0/9) * (fahrenheit - 32)
    return celcius

# Test
c1 = fahrenheit2celcius(32)
c2 = fahrenheit2celcius(212)
print c1, c2

# Convert fahrenheit to kelvin
def fahrenheit2kelvin(fahrenheit):
    celcius = fahrenheit2celcius(fahrenheit)
    kelvin = celcius + 273.15
    return kelvin

k1 = fahrenheit2kelvin(32)
k2 = fahrenheit2kelvin(212)
print k1, k2

# print hello world!
def hello():
    print "hello world"
    
#test
hello()

#
##
### More operations
##
#

#remainder - modular arithmetic
num = 49
tens = num // 10
ones = num % 10
print tens, ones
print 10* tens + ones

# Compute time on a 24hour clock
hour = 20
shift = 8
print (hour + shift) % 24

# Spaceship wraparound
width = 800
position = 2
move = -5
position = (position + move) % width
print position

#Data conversion operations
hour = 3
ones = hour % 10
tens = hour // 10
print tens, ones , ":00"
print str(tens), str(ones), ":00"
print str(tens) + str(ones) + ":00"

#
##
### Logic
##
#

a = True
b = False
c = True
d = False
print a, b

print "==="

print not a
print a and b
print a or b

print "==="
print (a and b) or (c and (not d))

#comparison operators
print "===="
#>
#<
#>=
#<=
#==
#!=

a = 7 > 3
print a
x = 5 
y = 5
b = x > y 
print b

c = "Hello" == "Hello"
print c

d = 20.6 <= 18.3
print d
print (a and b) or (c and (not d))

#
##
### Conditionals
##
#
#function to give money if you meet a friend
def greet(friend, money):
    if friend and (money > 20):
        print "Hi!"
        money = money - 20
    elif friend:
        print "hello"
    else: 
        print "haha" 
        money = money + 10
    return money

money = 15

money = greet(True, money)
print "Money:", money
print ""

money = greet(False, money)
print "Money:", money
print ""

money = greet(True, money)
print "Money:", money
print ""

#function to test if a year is a leap year
def is_leap_year(year):
    if (year % 400) == 0:
        return True
    elif (year % 100) ==0:
        return False
    elif (year % 4) == 0:
        return True
    else:
        return False
    
year = 2016
leap_year = is_leap_year(year)
if leap_year:
    print year, "is a leap year"
else:
    print year, "is not a leap year"


p = False
q = False
print not(p or not q)

def do_stuff():
    print "Hello world"
    return "Is it over yet?"
    print "Goodbye cruel world!"
    
print do_stuff()

n = 123

print(n - n % 10) / 10
print((n - n % 10) / 10) % 10
print((n - n % 10) % 100) / 10
 
import random
print random.randint(0, 10)
print random.randrange(0, 10)

#
##
###Programming tips
##
#

def volume_cube(side):
    return side ** 3

s = 2
print "Volume of cube with side", s, "is", volume_cube(s)

import random
    
def random_dice():
    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    return die1 + die2

print "Sum of two random dice, rolled once:", random_dice()
print "Sum of two random dice, rolled again:", random_dice()
print "Sum of two random dice, rolled again:", random_dice()

import math

def volume_sphere(radius):
    return 4.0/3.0 * math.pi * (radius ** 3)

r = 2
print "Volume of sphere of radius", r, "is", volume_sphere(r), "."

def area_triangle(base, height):
    return 0.5 * base * height

b = 5
h = 2 + 2
print "Area of triangle with base", b, "and height", h, "is", area_triangle(b,h), "."


def is_mary(x):
    if x == "Mary":
        print "Found Mary!"
    else:
        print "No Mary."

is_mary("Mary")
is_mary("Fred")

print "==="

def import_triangle_sss(side1, side2, side3):
    """
    Returns the area of a triange given the lengths of it's 
    three sides.
    """
    # Heron's formula
    semi_perim = (side1+side2+side3)/2.0
    return math.sqrt(semi_perim *
                     (semi_perim-side1) *
                     (semi_perim-side2) *
                     (s-side3))

###f(x) = -5 x5 + 69 x2 - 47

def quiz_func(x):
    return -5*x**5+69*x**2-47
print quiz_func(0), quiz_func(1), quiz_func(2), quiz_func(3)


def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    
    #PV (1+rate)periods
    # Put your code here.
    return present_value * (1+rate_per_period)**periods

print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)
print future_value(500, .04, 10, 10)

import math
print"==="
#Q8
#¼ n s2 / tan(π/n).
def polygon_area(n, s):
    return 0.25 *n*s**2 / math.tan(math.pi/n)
    
n=7.0
s=3.0
print polygon_area(n, s)

#Q9
def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_3(a, b, c):
    return max_of_2(a, max_of_2(b, c))
#Q10
def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale
    
project_to_distance(2, 7, 4)























