'''
Topic: While loops -- summation, counting, exponentiation, and "mystery" accumulator problems
'''

#######################################
# Sum up to n
#######################################
def sum_up(n):
    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1
    return sum
print(sum_up(5))
#######################################
# Sum from bottom to top
#######################################
def sum_up2(bottom, top):
    sum = 0
    i = bottom
    while i <= top:
        sum += i
        i += 1
    return sum
print(sum_up2(15, 19))
#######################################
# Sum multiples of 5
#######################################
def sum_fivers(n):
    sum = 0
    i = 5
    while i <= n:
        sum += i
        i += 5
    return sum
print(sum_fivers(10))
#######################################
# Count multiples of 5
#######################################
def count_fivers(n):
    count = 0
    i = 5
    while i <= n:
        count += 1
        i += 5
    return count
print(count_fivers(40))
#######################################
# Power using while-loop
#######################################
def power_up(base, exp):
    result = 1
    counter = 0
    while counter < exp:
        result *= base
        counter += 1
    return result
print(power_up(5, 5))
#######################################
# Mystery sum
#######################################
def mystery_sum(n):
    total = 0
    i = 1
    while i < n:
        if i % 2 == 0:
            total += i ** 2
        else:
            total += 2 * i
        i += 1
    return total
print(mystery_sum(13))
#######################################
# Mystery sum 2
#######################################
def mystery_sum2(n):
    total = 0
    i = 1
    while i < n:
        if i % 2 == 0:
            total += (i // 2) ** 2
        else:
            total += i ** 2
        i += 1
    return total
print(mystery_sum2(13))
#######################################
# Compare mystery sums
#######################################
def bigger_mystery(n):
    sum1 = mystery_sum(n)
    sum2 = mystery_sum2(n)
    if sum1 > sum2:
        return "ONE"
    elif sum2 > sum1:
        return "TWO"
    else:
        return "SAME"
print(bigger_mystery(20))
