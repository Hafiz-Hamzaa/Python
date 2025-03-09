# Functions in Python
# Block of statements that perform a specific task. we use function to reduce redundation
def print_hello():
    print("Hello")
print_hello()
print(print_hello()) # agr hamara function kuch return nh krta to output me None aiga

# calculate sum
def calc_sum(a , b):
    return a + b
sum = calc_sum(10 , 90)
print(sum)

# average of three numbers
def calc_avg(a , b , c):
    sum = a + b + c
    avg = sum / 3
    return avg
avg = calc_avg(2 , 2 , 8)
print(avg)

# we have two types of functions => built-in function (print , len , range , type) or user-defined function
# Default Parameters
# Assigning a default value to parameter, which is used when no argument is passed.
def mult(a = 12 , b = 2):
    return a * b
mult = mult()
print(mult)

# Lets Practice
# WAF to print the length of a list. ( list is the parameter)
cities = ["karachi" , "lahore" , "quetta" , "multan"]
def print_len(list):
    return len(list)
length = print_len(cities)
print(length)

# WAF to print the elements of a list in a single line. ( list is the parameter)
fruits = ["mango" , "apple" , "banana" , "pear" , "orange"]
def print_list(list):
    return list
listed = print_list(fruits)
print(listed)

# WAF to find the factorial of n. (n is the parameter)
def calc_fact(n):
    fact = 1
    for i in range(1 , n+1):
        fact *= i
    return fact
factorial = calc_fact(5)
print(factorial)

# WAF to convert USD to INR.
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val , "USD =" , inr_val , "INR")
converter(2)

# Recursion
# When a function calls itself repeatedly.
def show(n):
    if(n == 0): # Base Case
        return
    print(n)
    show(n-1)
show(5)

# lets practice
# Write a recursive function to calculate the sum of first n natural numbers.
def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n
sum = calc_sum(7)
print(sum)