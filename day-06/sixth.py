# Loops 
# Loops are used to repeat instructions.
count = 1 # iterator
while count <= 5: # iteration jb tk hoti rahai gi jb tak condition false na hojai
    print("hello")
    count += 1

# Lets create some question by using while loop :
# Print numbers from 1 to 100
i = 1
while i <= 100:
    print("i =", i)
    i += 1

# Print numbers from 100 to 1
j = 100
while j >= 1:
    print("j =", j)
    j -= 1

# Print the elements of the following list using a loop:
# jb bh ham kisi list ya  tuple kai aik aik element kai uper ja rahai hote hai usko ham "traverse" kehte hai mtlb travel krte hai
list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
idx = 0
while idx < len(list):
    print(list[idx])
    idx += 1

# Take input a number from user and Print the multiplication table of a number n.
# n = int(input("enter a number :"))
# num = 1
# while num <= 10:
#     print(n * num)
#     num += 1

# Search for a number x in this tuple using loop:
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
i = 0
x = 81
while i < len(tup):
    if(tup[i] == x):
        print("Found number at idx",i)
        break
    i += 1

# Break & Continue
# Break : used to terminate the loop when encountered.
i = 1
while i <= 10:
    print(i)
    if(i == 5):
        break
    i += 1

# Continue : terminates execution in the current iteration & continues execution of the loop with the next iteration.
i = 1
while i <= 5:
    if(i == 3):
        i += 1
        continue # skip hogya three
    print(i)
    i += 1

# lets check odd number by using continue 
j = 1
while j <= 10:
    if(j % 2 == 0):
        j += 1
        continue
    print(j)
    j += 1

# For Loops are used used for sequential traversal. For traversing list, string, tuples etc.
list = ["cake" , "mango" , "pear" , "orange"]
for ele in list:
    print(ele)

# for Loop with else
str = "python"
for char in str:
    print(char)
else:
    print("End")

# Print the elements of the following list using a for loop:
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
for val in nums:
    print(val)

# Search for a number x in this tuple using loop:
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
x = 25
for val in nums:
    if(val == x):
        print("Found")
        break
    print(val)

# range( )
# range(start?, stop, step?)
# Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default)
for val in range(20):
    print(val)

# Lets practice using for & range()
# Print numbers from 1 to 100.
for i in range(1 , 101):
    print(i)

# Print numbers from 100 to 1.
for i in range(100 , 0 , -1):
    print(i)

# Print the multiplication table of a number n.
for j in range(2 , 21 , 2):
    print(j)

# pass Statement
# pass is a null statement that does nothing. It is used as a placeholder for future code.
for ele in range(10):
    pass
print("doing in future")

# Lets Practice
# WAP to find the sum of first n numbers. (using while)
n = 5
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print("total sum =", sum)

# WAP to find the factorial of first n numbers. (using for)
n = 5
i = 1
fact = 1
while i <= n:
    fact *= i
    i += 1
print("factorial =", fact)