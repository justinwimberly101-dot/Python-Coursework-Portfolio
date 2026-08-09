'''
Topic: Using pre-written functions -- parameters, return values, calling functions
'''

#################################################
###        Provided helper functions          ###
#################################################
def largest(x, y, z):
    if (x >= y) and (x >= z):
        return x
    if (y >=x) and (y >= z):
        return y
    return z

def average_three(a,b,c):
    return (a+b+c)/3

def mystery_fn(a,b,c):
    return (b//c)*(c%b)

def odd_or_even(the_num):
    if (the_num%2)==0:
        result = "even"
    else:
        result = "odd"
    return result
##### END OF helper functions ############


##################################################
###                   Driver code              ###
##################################################

# Task 1: Getting values from user
####################################
int1 = int(input("What is the first integer?"))
int2 = int(input("What is the second integer?"))
int3 = int(input("What is the third integer?"))
float1 = float(input("What is the first float?"))
float2 = float(input("What is the second float?"))
float3 = float(input("What is the third float?"))

##  Task 2: find the largest
#############################
print("Largest is:", largest(5, 12, 9))
print("Largest is:", largest(int1, int2, int3))
print("Largest is:", float(largest(float1, float2, float3)))
print()
##  Task 3: average of 3
#############################
print("The average is:", round(average_three(2.009, 19.7, 12.002), 3))
print("The average is:", round(average_three(int1, int2, int3), 1))
print("The average is:", round(average_three(float1, float2, float3), 2))
print()

## Task 4: Mystery
###############################
print("The mystery result is:", mystery_fn(int1, int2, int3))
print("The mystery result is:", mystery_fn(int3, int1, int2))
print("The mystery result is:", mystery_fn(int1, int1, int1))
print()

## Task 5: test odd/even
###############################
print(int1, "is", odd_or_even(int1))
print(int2, "is", odd_or_even(int2))
print(int3, "is", odd_or_even(int3))
print()
## Task 6: test odd/even on results of mystery_fn()
###############################
print("First result is", odd_or_even(mystery_fn(int1, int2, int3)))
print("Second result is", odd_or_even(mystery_fn(int3, int1, int2)))
print("Third result is", odd_or_even(mystery_fn(int1, int1, int1)))
