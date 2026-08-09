'''
Topic: Nested (2D) lists -- merging, combinations, counting across sublists, shape checks
'''

#######################################
# Merge two name lists, skipping duplicates
#######################################
def merge_namelist(namelst1, namelst2):
    merged = []

    for name in namelst1:
        merged.append(name)

    for name in namelst2:
        if name not in merged:
            merged.append(name)

    return merged

print(merge_namelist(["Hanna", "Jaime"], ["Hanna", "Lynn"]))
print()


#######################################
# Build every flavor/topping combo
#######################################
def menu(flavors, toppings):
    combos = []

    for f in flavors:
        for t in toppings:
            combos.append(f + " " + t)

    return combos

print(menu(["Vanilla", "Chocolate"], ["Sprinkles", "Almonds"]))
print()


#######################################
# Count occurrences of one name
#######################################
def count_one_name(all_names, common_name):
    count = 0

    for name in all_names:
        if name == common_name:
            count += 1

    return count

print(count_one_name(["Earl", "Cathy", "Petra", "Earl"], "Petra"))
print()


#######################################
# Count occurrences across multiple target names
#######################################
def count_many_names(all_names, common_names):
    total = 0

    for common in common_names:
        count = 0
        for name in all_names:
            if name == common:
                count += 1
        total += count

    return total

print(count_many_names(["Earl", "Petra", "Earl", "Jane", "Jane"], ["Earl", "Jane"]))
print()


#######################################
# Sum all numbers across a list of lists
#######################################
def sum_up(list_of_lists):
    total = 0

    for mini in list_of_lists:
        for num in mini:
            total += num

    return total

print(sum_up([[3, 4], [1, 1, 1]]))
print()


#######################################
# Find the largest value across a list of lists
#######################################
def find_largest(list_of_lists):
    first_value_found = False
    maxx = 0

    for mini in list_of_lists:
        for num in mini:
            if not first_value_found:
                maxx = num
                first_value_found = True
            elif num > maxx:
                maxx = num

    return maxx

print(find_largest([[1, 2], [10], [3]]))
print()


#######################################
# Check whether a 2D list is square (NxN)
#######################################
def is_square(twoD_list):
    rows = len(twoD_list)

    for row in twoD_list:
        if len(row) != rows:
            return False

    return True

print(is_square([[1,2,3],[4,5,6],[7,8,9]]))
print(is_square([[1,2],[3,4,5]]))
print()
