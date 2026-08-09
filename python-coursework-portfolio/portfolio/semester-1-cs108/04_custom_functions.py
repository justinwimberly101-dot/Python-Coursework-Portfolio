'''
Topic: Writing original functions from a spec (unit conversion, geometry, pricing math)
'''

# cm_to_in: converts centimeters to inches, rounded to the nearest tenth.
# NOTE: 1 inch = 2.54 centimeters
def cm_to_in(c):
    inches = c / 2.54
    return round(inches, 1)

# print(cm_to_in(7.6))
# print(cm_to_in(3.2))
# print(cm_to_in(12.34))
#######################################

# rect_perimeter: returns the perimeter of a rectangle given length and width.
def rect_perimeter(l, w):
    return 2*l + 2*w

# print(rect_perimeter(2,3))
# print(rect_perimeter(8,5))
# print(rect_perimeter(12,21))
#######################################

# avg_six: finds the average (mean) of six values, rounded to the nearest tenth.
def avg_six(a, b, c, d, e, f):
    avg = (a+b+c+d+e+f)/6
    return round(avg, 2)

# print(avg_six(2,7,8,12,14,20))
# print(avg_six(3,4,5,10,14,15))
# print(avg_six(1,7,5,23,30,31))
#######################################

# reliant_num: returns x^y - y
def reliant_num(x, y):
    return x**y - y

# print(reliant_num(20,7))
# print(reliant_num(13,3))
# print(reliant_num(6,9))
#######################################

# speaker_price: calculates the price of a bluetooth speaker after a
# discount, then applies tax. Discount is applied before tax.
def speaker_price(price, discount_percent, tax_rate):
    y = discount_percent/100.0
    z = tax_rate/100.0
    final_price = price * (1 - y) * (1 + z)
    return round(final_price, 2)

# print(speaker_price(112.99, 20, 5))
# print(speaker_price(121.99, 10, 4))
# print(speaker_price(133.99, 40, 3))
#######################################

# cups_to_sleeves: returns number of sleeves needed (50 cups each, always round up).
def cups_to_sleeves(a):
    sleeves = a / 50
    if sleeves == int(sleeves):
        return int(sleeves)
    else:
        return int(sleeves) + 1

# print(cups_to_sleeves(165))
# print(cups_to_sleeves(130))
# print(cups_to_sleeves(70))
#######################################

# determinant: returns the discriminant of a quadratic (b^2 - 4ac).
def determinant(a, b, c):
    return b**2 - (4*a*c)

# print(determinant(4,2,8))
# print(determinant(3,7,5))
# print(determinant(9,5,9))
