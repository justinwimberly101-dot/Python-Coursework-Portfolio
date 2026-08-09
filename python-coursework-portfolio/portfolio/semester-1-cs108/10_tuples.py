'''
Topic: Tuples -- immutability, building tuples manually, and tuple-returning functions
'''

#######################################
# Find (smallest, largest) in a list
#######################################
def extremes(my_list):
    if my_list == []:
        return None
    if len(my_list) == 1:
        return (my_list[0], None)

    smallest = my_list[0]
    largest = my_list[0]

    for num in my_list:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return (smallest, largest)

#######################################
# Find the range (largest - smallest) of a list
#######################################
def find_range(my_list):
    vals = extremes(my_list)
    if vals is None or vals[1] is None:
        return None
    return vals[1] - vals[0]

#######################################
# Return a tuple of sublist lengths
#######################################
def lengths(nested_list):
    result = ()
    for sub in nested_list:
        count = 0
        for _ in sub:
            count += 1
        result += (count,)
    return result

#######################################
# Count vowels, returned as a tuple (a, e, i, o, u)
#######################################
def count_vowels(my_list):
    a = e = i = o = u = 0

    for ch in my_list:
        if ch == 'a':
            a += 1
        elif ch == 'e':
            e += 1
        elif ch == 'i':
            i += 1
        elif ch == 'o':
            o += 1
        elif ch == 'u':
            u += 1

    return (a, e, i, o, u)

#######################################
# Reverse a tuple into a list
#######################################
def backwards(my_tuple):
    result = []
    idx = len(my_tuple) - 1
    while idx >= 0:
        result.append(my_tuple[idx])
        idx -= 1
    return result

#######################################
# Generate a sequence between two tuple values
#######################################
def generate_sequence(my_tuple):
    a, b = my_tuple
    start = min(a, b)
    end = max(a, b)

    result = []
    while start <= end:
        result.append(start)
        start += 1
    return result

#######################################
# Count distinct elements in a tuple
#######################################
def count_distinct_elements(my_tuple):
    if my_tuple == ():
        return None

    seen = ()
    for item in my_tuple:
        duplicate = False
        for val in seen:
            if item == val:
                duplicate = True
        if duplicate == False:
            seen += (item,)
    return len(seen)

#######################################
# Largest absolute difference across a list of (a, b) tuples
#######################################
def largest_difference(my_list):
    first = True
    largest = 0

    for a, b in my_list:
        diff = abs(a - b)

        if first:
            largest = diff
            first = False
        elif diff > largest:
            largest = diff

    return largest
