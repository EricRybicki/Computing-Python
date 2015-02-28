###An Introduction to Interactive Programming in Python (Part 1) 
##Week 0
#Operations, expressions, and assignments

# Arithmetic expressions - numbers, operators, expressions

print 3, -1, 3.14159, -2.8

# numbers - two types, an integer or a decimal number
# two corresponding data types int() and float()

print type(3), type(3.14159)
print type(3.0)


# we can convert between data types using int() and float()
# note that int() takes the "whole" part of a decimal number and doesn't round
# float() applied to integers is boring

print int(3.14159), int(-2.8)
print float(3), float(-1)


# floating point number have around 15 decimal digits of accuracy
# pi is 3.1415926535897932384626433832795028841971...
# square root of two is 1.4142135623730950488016887242096980785696...

# approximation of pi, Python displays 12 decimal digits

print 3.1415926535897932384626433832795028841971

# appoximation of square root of two, Python displays 12 decimal digits

print 1.4142135623730950488016887242096980785696

# arithmetic operators
# +		plus		addition
# -		minus		subtraction
# *		times		multiplication
# /		divided by 	division
# **    power		exponentiation

print 1 + 2, 3 - 4, 5 * 6, 2 ** 5

# Division in Python 2
# If one operand is a decimal (float), the answer is decimal

print 1.0 / 3, 5.0 / 2.0, -7 / 3.0

# If both operands are ints, the answer is an int (rounded down)

print 1 / 3, 5 / 2, -7 / 3


# expressions - number or a binary operator applied to two expressions
# minus is also a unary operator and can be applied to a single expression

print 1 + 2 * 3, 4.0 - 5.0 / 6.0, 7 * 8 + 9 * 10

# expressions are entered as sequence of numbers and operations
# how are the number and operators grouped to form expressions?
# operator precedence - "please excuse my dear aunt sallie" = (), **, *, /, +,-

print 1 * 2 + 3 * 4
print 2 + 12


# always manually group using parentheses when in doubt


print 1 * (2 + 3) * 4
print 1 * 5 * 4


# variables - placeholders for important values
# used to avoid recomputing values and to
# give values names that help reader understand code


# valid variable names - consists of letters, numbers, underscore (_)
# starts with letter or underscore
# case sensitive (capitalization matters)

# legal names - ninja, Ninja, n_i_n_j_a
# illegal names - 1337, 1337ninja

# Python convention - multiple words joined by _
# legal names - elite_ninja, leet_ninja, ninja_1337
# illegal name 1337_ninja



# assign to variable name using single equal sign =
# (remember that double equals == is used to test equality)

# examples 

my_name = "Eric Rybicki"
print my_name

my_age = 29
print  my_age

# birthday - add one

my_age += 1
print my_age


# the story of the magic pill

magic_pill = 30
print my_age - magic_pill

my_grand_dad = 74
print my_grand_dad - magic_pill * 2
print "pause"

# Temperature examples

# convert from Fahrenheit to Celsuis
# c = 5 / 9 * (f - 32)
# use explanatory names

temp_Fahrenheit = 212

temp_Celsius = 5.0 / 9.0 * (temp_Fahrenheit - 32)

print temp_Celsius

# test it! 32 Fahrenheit is 0 Celsius, 212 Fahrenheit is 100 Celsius


# convert from Celsius to Fahrenheit
# f = 9 / 5 * c + 32

temp_Celsius = 100

temp_Fahrenheit = 9.0 / 5.0 * temp_Celsius + 32

print temp_Fahrenheit


# test it!

