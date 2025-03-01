# Python is indentation languea means put proper spacing insted of curly {} braces put 4 space
# Types of Operators
# An operator is a sybol that perform certain operation between operands
# Arithemtic Operators => + , - , * , / , % , **
val1 = 2
val2 = 2
print(val1 + val2)
print(val1 ** val2)
print(val1 % val2)

# Relational / Comparision Operator =>  == , != , < , > , <= , >=
num1 = 20
num2 = 30
print(num1 == num2)
print(num2 > num1)

# Assignment Operator => = , += , -= , *= , /= , %= , **=
num1 = 80
num1 += 20
print(num1)

# Logical Operaor => not , and , or
val1 = True
val2 = False
print(not val1)
print(val1 == val2 and val2 != val1)
print(val1 == val2 or val2 != val1)

# Conditional Statements => if , elif , else
# Traffic Light Code
light = input("light color :")
if(light == "red"): # after colon : give 4 spaces 
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("get ready")
else:
    print("light is broken")

# Grade of Students
marks = int(input("marks :"))
if(marks >= 90):
    print("Grade A")
elif(marks >= 80 and marks < 90):
    print("Grade B")
elif(marks >= 70 and marks < 80):
    print("Grade C")
else:
    print("Grade D")

# Print Output for:
# A = 5 & G = M
# A = 2 & G = F
A = int(input("A : "))
G = input("M/F : ")
if((A == 1 or A == 2) and  G == "M"):
    print("fee is 100")
elif(A == 3 or A == 4 or G == "F"):
    print("fee is 200")
elif(A == 5 or G == "M"):
    print("fee is 300")
else:
    print("no fee")

# Single Line => Ternary Operator
food = input("food :")
eat = "Yes" if food == "cake" else "no"
print(eat)

# direct write statement
fruits = input("fruits :")
print("sweet") if fruits == "mango" or fruits == "grapes" else print("not sweet")

# Clever if Ternary Operator => use for small program to check one condition
vege = input('Vegetable: ')
eat = ('no', 'yes')[vege == "carrot"] 
print(eat)

# Best Practices 
# Simple Instructions
# Use appropriate cooments
# short & meaningful variables
# One instruction per task
# avoid comple expression

# Type Conversion => python automatically convert one type into another type
a = 20
b = 2.34
c = a + b
print(c)

# Type Casting => we convert one type into another type by manually
a = int("2")
b = 12
c = a + b
print(c)

# Lets Practice
# Write a Program to input 2 numbers & print their sum.
num1 = int(input("Enter a first number :"))
num2 = int(input("Enter a second number :"))
result = num1 + num2
print("The sum of two number is :", result)

# WAP to input side of a square & print its area.
side = int(input("Enter a side of a square :"))
area = side * side
print("The area is :",area)

# WAP to input 2 floating point numbers & print their average.
a = float(input("First Number :"))
b = float(input("Second Number :"))
output = (a + b) / 2
print(output)

# WAP to input 2 int numbers, a and b.
# Print True if a is greater than or equal to b. If not print False.
a = int(input("First :"))
b = int(input("Second :"))
result = "True" if a >= b else "False"
print(result)