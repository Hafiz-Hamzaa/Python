# First You have to inStall python latest version 

""" What is Python?
Python is simple & easy
Free & Open Source
High Level Language
Developed by Guido van Rossum
Portable means run python code in every operating system like mac , linux etc """

# Our First Program
print("Hello World")

"""Python Character Set
Letters : A to Z, a to z
Digits : 0 to 9
Special Symbols - + - * / etc.
Whitespaces : Blank Space, tab, carriage return, newline, formfeed"""

# Variable Rules for Identifier
# Dont start with digit 
# We cannot use special symbol like $,&,@ except only underscore(_)

# Variables => A variable is a name given to a memory location in a program.
name = "Hamza"
age = 15
price = 60
cost = 20.9
color = None
print(name)
print(age)
print(price,cost) # 60 20.9

""" Data Types
Integers => 20 , -90 , 0
String => '' , "" , """"""
Float => 19.5 , 70.5
Boolean => True , False
None => None  """

# check the variable data type by using type keyword
print(type(name))
print(type(age))
print(type(price))
print(type(cost))
print(type(color))

# print sum
print(20 + 35)
num1 = 50
num2 = 80
total_sum = num1 + num2
total_sum = num1 - num2
print(total_sum)

# Keywords => Keywords are reserved words in python like elif , else , for , while , True , False , yield etc.
# Comments in Python => Code Readability
# Single Line Comment => # This is a single line comment
# Multi Line Comment => """ This is a Multi Line Comment """

# Types of Tokens => Punctuators are symbols to organize code sentence structure in programing.
# () , [] , {} , @ , # etc.

# Python is implicit Typed Language => means btana nh parta is variable me kia data type hai internalyy khud hi usko wo detect krltea hai kai isme kai data type hai

# Expression Executation
# First Rule : Strings & Numeric values can operate together with *
A,B = 2,3
Txt = "@"
print(2 * Txt * 3) # @@@@@@ mtlb string 6 times repeate krdo

# Second Rule : String & String can operate with + or called concatenation
A,B = "2",3
Txt = "@"
print((A + Txt) * B) # 2@2@2@

# Third Rule : Numeric values can opearte with all arithmetic operators (+,-,*,/,//,**,%)
A,B = 3,4
C = 6
print(A + B * C) # According to BODMAS Rule first multiplu then sum : 27

# Fourth Rule : Arithmetic Expresssion with integer and float will result in float
A,B = 10,5.0
C = A * B
print(C) # 50.0

# fIFTH Rule : Result of Division Operator with two integers will be float
A,B = 1,2
C = A / B
print(C) # 0.5

# Sixth Rule : Integer Divison means ( // ) with float and int will give int bu display as float
# ye result me deta to int hai lekin display float krta hai mtlb int ko convert krdeta hai float me closest nummber yani small number me round off krkai kon integer division ( // )
# age normal disvison krte jese ( / ) ye direct float hi deta hai
A,B = 1.5,3
C = A // B
print(C , A / B) # 0.0 , 0.5

# Integer Division Rule :
# Result of A // B is same as floor A / B
# floor gives closest integer which is less then or equal to the float value like : 2.4 = 2 , -5.2 = -6 , 7.0 = 7 , 2 = 2
A,B = 12,5
C = A // B
print(C) # 2 wese to iska answer A / B = 2.4 tha lekin closets integer kia hogya iska 2

A,B = -12,5
C = A // B
print(C) # -3

# Remainder is negative when denominator is negative mtlb => 5/-2
A,B = 5,-2
C = A % B
print(C) # -1

# input in python => input statements is ued to accept values from user
name = input("name :") # input string
age = int(input("age :")) # int input
price = float(input("price :")) # float input
print("My name is", name ,"I am", age , "years old", "The price of T-Shirts is",price)

# Practice Time
# State True or False
# 1- /* is a symbol used in python for single comment = False
# 2- 2ndName is an invlaid identifier in python = True
# 3- ** is a valid arithmetic operator in python = True
# 4- in is a logical operator in python = False
# variable declaratio is implicit in python = True
# 6- Consider the given exprssion : not True and False or True
# Operator Prescedence => not > and > or
# Whic is the correct : a) True  b) False  c) NONE  D) NULL
# Option A is correct