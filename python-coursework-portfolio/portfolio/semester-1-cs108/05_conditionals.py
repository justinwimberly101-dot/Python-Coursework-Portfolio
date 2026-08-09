'''
Topic: Conditionals -- if/elif/else logic across a variety of small problems
'''

def ab_val(num):
    if num<0:
        return num*-1
    else:
        return num
print(ab_val(5))
print(ab_val(-2))
print(ab_val(-5))
###############################################
def circ_calc(radius, measure):
    pi = 3.14159
    if measure == 'c':
        result = 2 * pi * radius
    elif measure == 'a':
        result = pi * radius ** 2
    elif measure == 'v':
        result = (4/3) * pi * radius ** 3
    else:
        return -1

    return round(result, 3)
print(circ_calc(3, 'c'))
print(circ_calc(6, 'a'))
print(circ_calc(7, 'v'))
print(circ_calc(2, 'x'))
###############################################
def discriminant(a, b, c):
    return b**2 - 4*a*c

def kind_of_roots(a, b, c):
    disc = discriminant(a, b, c)
    if disc > 0:
        return "two real"
    elif disc == 0:
        return "one real"
    else:
        return "two imaginary"

print(kind_of_roots(1, 0, -9))
print(kind_of_roots(1, 2, 1))
print(kind_of_roots(1, 2, 9))
###############################################
def stock_advice(purchase_price, current_price):
    change = (current_price - purchase_price) / purchase_price
    if change > 0.3:
        return "BUY"
    elif change <= -0.5:
        return "SELL"
    else:
        return "HOLD"

print(stock_advice(250.09, 466.75))
print(stock_advice(100, 40))
print(stock_advice(100, 120))
###############################################
def level_up(points, current_level):
    next_level = current_level + 1
    return points > 100 * next_level

print(level_up(450, 3))
print(level_up(345, 7))
###############################################
def level_up2(points, current_level, expert_level):
    next_level = current_level + 1
    if expert_level == 'beginner':
        return points > 100 * next_level
    elif expert_level == 'intermediate':
        return points > 200 * next_level
    elif expert_level == 'expert':
        return points > 500 * next_level
    elif expert_level == 'pro':
        return points > 1000 * next_level
    else:
        return False

print(level_up2(4550, 8, 'expert'))
print(level_up2(5350, 11, 'pro'))
