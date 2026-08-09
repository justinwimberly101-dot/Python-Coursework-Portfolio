'''
Topic: For loops -- range-based summation, factor counting, iterating over lists
'''

#######################################
# Sum from 1 to n
#######################################
def sum_from_one(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total
print(sum_from_one(6))

#######################################
# Sum of even numbers up to n
#######################################
def sum_evens(n):
    total = 0
    for i in range(2, n+1, 2):
        total += i
    return total
print(sum_evens(6))

#######################################
# Sum from bottom to top (for-loop version)
#######################################
def sum_up_again(bottom, top):
    total = 0
    for i in range(bottom, top+1):
        total += i
    return total
print(sum_up_again(7, 14))

#######################################
# Count proper factors of n
#######################################
def count_prop_facs(n):
    count = 0
    for i in range(1, n):
        if n % i == 0:
            count += 1
    return count
print(count_prop_facs(16))

#######################################
# Sum all elements in a list
#######################################
def add_elems(num_list):
    total = 0
    for num in num_list:
        total += num
    return total
print(add_elems([1,2,12,48,64]))

#######################################
# Count zeros in a list
#######################################
def count_zeros(num_list):
    count = 0
    for num in num_list:
        if num == 0:
            count += 1
    return count
print(count_zeros([1,1, 0, 4, 0, 0, 2]))
