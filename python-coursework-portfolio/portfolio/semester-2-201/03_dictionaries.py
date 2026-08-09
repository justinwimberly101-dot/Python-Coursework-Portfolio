'''
Topic: Dictionaries -- grouping, merging with sets, nested dict/list
structures, and inverting a dictionary
'''

##############################################
def make_group(myDict):
##############################################
    result = [[]]

    for key in myDict:
        group_num = myDict[key]

        while len(result) <= group_num:
            result.append([])

        result[group_num].append(key)

    return result


##############################################
def display_info(lst):
##############################################
    result = {}

    for i in range(len(lst)):
        name = lst[i][0]
        department = lst[i][1]
        grades = lst[i][2]

        result[name] = {}
        result[name]['department'] = department
        result[name]['grades'] = grades

    return result


##############################################
def merge_dicts(d1, d2):
##############################################
    result = {}

    for key in d1:
        result[key] = set()

        for item in d1[key]:
            result[key].add(item)

    for key in d2:
        if key not in result:
            result[key] = set()

        for item in d2[key]:
            result[key].add(item)

    return result


##############################################
def update_inventory(inventory):
##############################################
    result = {}

    for row in inventory:
        products = inventory[row]

        for product in products:
            quantities = products[product]
            total = 0

            for i in range(len(quantities)):
                total = total + quantities[i]

            if product not in result:
                result[product] = total
            else:
                result[product] = result[product] + total

    return result


##############################################
def swap(d):
##############################################
    new_dict = {}

    for student in d:
        grades = d[student]

        for i in range(len(grades)):
            grade = grades[i]

            if grade not in new_dict:
                new_dict[grade] = []

            if student not in new_dict[grade]:
                new_dict[grade].append(student)

    d.clear()

    for grade in new_dict:
        d[grade] = new_dict[grade]
