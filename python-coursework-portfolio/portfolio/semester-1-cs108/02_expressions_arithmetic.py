'''
Topic: Expressions, the quadratic formula, and floor division / modulo
'''

####################################
# Task 1: Average of six test scores
####################################
test1 = 99
test2 = 89
test3 = 86
test4 = 88
test5 = 92
test6 = 95
avg = (test1 + test2 + test3 + test4 + test5 + test6) / 6

print("The average is", avg, ".")
print()
####################################
# Task 2: Quadratic roots
####################################
a = 1
b = 0
c = -9
Root1 = ((b * -1) + (b**2  - 4 * a * c)**(1/2))/ (2 * a)
Root2 = ((b * -1) - (b**2  - 4 * a * c)**(1/2))/ (2 * a)

print("The first root is", Root1, ".")
print("The second root is", Root2, ".")
print()
####################################
# Task 3: Quadratic roots (second example)
####################################
a = 1
b = -10
c = -24
Root3 = ((b * -1) + (b**2  - 4 * a * c)**(1/2))/ (2 * a)
Root4 = ((b * -1) - (b**2  - 4 * a * c)**(1/2))/ (2 * a)

print("The first root is", Root3, ".")
print("The second root is", Root4, ".")
print()
####################################
# Task 4: Inches to feet/inches conversion
####################################
a = 50
b = 100
c = 122
d = 8986
print( a, "inches is", a//12, "feet and", a%12, "inches.")
print( b, "inches is", b//12, "feet and", b%12, "inches.")
print( c, "inches is", c//12, "feet and", c%12, "inches.")
print( d, "inches is", d//12, "feet and", d%12, "inches.")
