# Strings & Conditional Statements
# strings => string is a data type that store a sequence of chracters
name = 'apple'
name = "apple"
name = """apple"""
print(name)

# Basic Operations
fruit = "mango"
print(len(fruit))

# concatenations with + operator
name = "Ali"
message = "My name\nis" # escape chracter
result = message + " " + name
print(result)

# Indexing
vegetable = "carrot"
print(vegetable[3]) # we cannot replace the chracter of any string by using index because strings are immutable

# Strings Functions
# Slicing => Accessing parts of string
transport = "corolla"
print(transport[2:2])
print(transport[:3]) # 0 : 3
print(transport[2:]) # extract with the end of string

# Negative Index => start with backword position
name = "hamza"
print(name[-4:-2])

#str.endsWith(“er.“) returns true if string ends with substr
str = "I am a coder"
print(str.endswith("er"))

#str.capitalize( ) capitalizes 1st char
message = "i am learning python"
print(message.capitalize())

#str.replace( old, new ) replaces all occurrences of old with new
mess = "i read a old book"
print(mess.replace("old","new"))

#str.find( word ) returns 1st index of 1st occurrence
word = "the more you learn the more you earn"
print(word.find("learn"))

#str.count(“am“) counts the occurrence of substr in string
message = "today a reader tommorrow a leader"
print(message.count("reader"))

# Nesting Conditional Statement
age = 75
if(age >= 60):
    if(age >= 70):
        print("cannot drive")
    else:
        print("can drive")

# Lets Practice
# WAP to input user’s first name & print its length.
name = input("enter a first name :")
print(len(name))

# WAP to find the occurrence of ‘$’ in a String.
str = "Hi $ I am the $ symbol"
print(str.count("$"))

# WAP to check if a number entered by the user is odd or even.
number = int(input("enter a number :"))
if(number % 2 == 0):
    print("user enetered a even number")
else :
    print("user enetered a odd number")

# WAP to find the greatest of 3 numbers entered by the user.
number = int(input("enter a number :"))
if(number > 3):
    print(number , "is greater then 3")
else:
    print(number , "is not greater then 3")

# WAP to check if a number is a multiple of 7 or not.
number = int(input("enter a random number :"))
if(number % 7 == 0):
    print(number , "is a multiple of 7")
else: 
    print(number , "is not a multiple of 7")