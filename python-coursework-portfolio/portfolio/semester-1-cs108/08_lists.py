'''
Topic: Lists -- indexing, mutation, filtering, and building new lists from old ones
'''

#######################################
# Sum all elements in a list
#######################################
def add_elems(num_list):
    total = 0
    for num in num_list:
        total += num
    return total
print(add_elems([1, 2, 3, 4, 5]))# 15

#######################################
# Total value of a list of coins
#######################################
def total_value(coins):
    total = 0
    for coin in coins:
        if coin == "penny":
            total += 1
        elif coin == "nickel":
            total += 5
        elif coin == "dime":
            total += 10
        elif coin == "quarter":
            total += 25
        elif coin == "dollar":
            total += 100
    return total

print(total_value(["penny", "nickel", "quarter"]))  # 31
#######################################
# Count nickels in a list
#######################################
def count_nickels(coin_list):
    count = 0
    for coin in coin_list:
        if coin == 'nickel':
            count += 1
    return count

print(count_nickels(['dime','nickel','nickel']))    # 2
#######################################
# Sum indices of even-valued elements
#######################################
def even_index_sum(num_lst):
    total = 0
    for i in range(len(num_lst)):
        if num_lst[i] % 2 == 0:
            total += i
    return total

print(even_index_sum([1,2,3,4,5,6]))                # 9
#######################################
# Halve even values in place
#######################################
def half_em(lst):
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst[i] = lst[i] // 2
    return lst

print(half_em([1,6,10,5]))                          # [1,3,5,5]
#######################################
# Filter to only negative numbers
#######################################
def only_negs(nums):
    negs = []
    for num in nums:
        if num < 0:
            negs.append(num)
    return negs

print(only_negs([-3,-1,2,6,8]))                     # [-3, -1]
#######################################
# Weighted average of midterm/final scores
#######################################
def calc_avgs(mid_scores_lst, final_scores_lst):
    avgs = []
    for i in range(len(mid_scores_lst)):
        avg = mid_scores_lst[i] * 0.4 + final_scores_lst[i] * 0.6
        avgs.append(round(avg, 1))
    return avgs

print(calc_avgs([80,80,60],[92,88,58]))             # [87.2, 84.8, 58.8]
#######################################
# Find indices where coin name matches its value
#######################################
def coin_matches(names_lst, values_lst):
    matches = []
    for i in range(len(values_lst)):
        name = names_lst[i]
        value = values_lst[i]

        if name == "penny" and value == 1:
            matches.append(i)
        elif name == "nickel" and value == 5:
            matches.append(i)
        elif name == "dime" and value == 10:
            matches.append(i)
        elif name == "quarter" and value == 25:
            matches.append(i)
        elif name == "dollar" and value == 100:
            matches.append(i)
    return matches

print(coin_matches(["dime","dime","nickel"],[10,10,5]))  # [0,1,2]
