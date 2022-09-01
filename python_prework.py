# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print(f"hello_{user_name}")

hello_name("Betty")

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for i in range(1,100,2):
        print(i)

first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    return max(a_list)

max_num_in_list([99,8,72,32,234])

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if a_year % 4 != 0:
        return False
    elif a_year % 4 == 0: 
        if a_year % 100 != 0:
            return True
        elif a_year % 100 == 0 and a_year % 400 == 0:
            return True
        else:
            return False

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    if a_list == list(range(a_list[0], a_list[-1] + 1)):
        return True     
    else:
        return False  
   
is_consecutive([1,2,3,4,5])
is_consecutive([9,3,6,4,5])
is_consecutive([7,8,9,10,11])
is_consecutive([7,8,90,10,11])
