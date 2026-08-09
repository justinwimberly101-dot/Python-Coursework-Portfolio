'''
Topic: Intro to print statements, variables, and basic arithmetic
'''

print("This is my first program.")
print("--------")        #section separator

#grocery list section
#####################
item1 = "milk"
item2 = "oats"
item3 = "dish soap"
item4 = "peanut butter"
print("Grocery List:", item1, "," , item2 ,",", item3, "," , item4)


print("--------")        #section separator

#ages section
#####################
my_age = 25
your_age = 16
age_sum = my_age + your_age
age_diff = my_age - your_age
print("The sum of your age and mine is", age_sum)
print("Our age difference is", age_diff)

print("--------")        #section separator

# temperatures section
######################
temp1 = 88.5
temp2 = 53.9
temp3 = 66.3
temp4 = 73.94
num_temps = 4
avg_temp = (temp1 + temp2 + temp3 + temp4) / num_temps
print("The average temperature is:", avg_temp)

print("--------")        #section separator

# pints and gallons
#######################
#NOTE: There are 4 quarts in a gallon
#      There are 8 pints in a gallon

gallons = 4
num_pints = gallons * 8
print(gallons, "gallons is equivalent to", num_pints, "pints.")

pints1 = 27
num_gallons = pints1 // 8
extra_pints = pints1 % 8
print(pints1, "pints is equivalint to", num_gallons, "gallons and", extra_pints, "additional pints.")

pints1 = 105
num_gallons = pints1 // 8
extra_pints = pints1 % 8
print(pints1, "pints is equivalint to", num_gallons, "gallons and", extra_pints, "additional pints.")

''' "Why did the computer scientist have their driver's license revoked?"
    Answer: "... because he kept crashing!"
'''
