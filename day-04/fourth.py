# List & Tuples in Python
# Lists in Python
# A built-in data type that stores set of values
# It can store elements of different types (integer, float, string, etc.)
marks = [23 , 34 , 78 , 90]
print(marks)
print(marks[2]) # indexing
print(len(marks)) # length of list
marks[0] = 20
print(marks) # allowed to change the value of list because list are mutable

# List Slicing =>  Similar to String Slicing
fruits = ["apple" , "mango" , "pear" , "orange"]
print(fruits[0:2])
print(fruits[:3]) # 0 : 3
print(fruits[1:]) # end of index
print(fruits[-3:-2]) # negative index

# List Methods
# list.append(4) #adds one element at the end
list = [2 , 1 , 3]
list.append(6)
print(list)

# list.sort( ) #sorts in ascending order
list = [42 , 35 , 60 , 76]
list.sort()
print(list)

# list.sort( reverse=True ) #sorts in descending order
list = [23 , 90 , 120 , 78]
list.sort(reverse=True)
print(list)

# list.reverse( ) #reverses list
list = [120 , 89 , 90 , 67]
list.reverse()
print(list)

# list.insert( idx, el ) #insert element at index
list = [120 , 130 , 140 , 150]
list.insert(2,200)
print(list)

# list.remove(1) #removes first occurrence of element
list = [1 , 2 , 3 , 4 , 5]
list.remove(2)
print(list)

# list.pop( idx ) #removes element at idx
list = [450 , 900 , 876 , 890]
list.pop(2)
print(list)

# Tuples in Python
# A built-in data type that lets us create immutable sequences of values.
tuple = (1 , 2 , 3 , 4)
tuple = (1,) # single value tuple create krna ho to single value kai sth comma (,) dena compulsory hai wrna python isko int smje ga
print(tuple)
print(type(tuple))

# Tuple Methods
# tup.index( el ) #returns index of first occurrence
tuple = [12 , 67 , 90 , 65]
print(tuple.index(67))

# tup.count( el ) #counts total occurrences
tuple = (120 , 890 , 765 , 345 , 120)
print(tuple.count(120))

# Let‘s Practice
# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
movies = []
movies.append(input("first movie :"))
movies.append(input("second movie :"))
movies.append(input("third movie :"))
print(movies)

# WAP to count the number of students with the “A” grade in the following tuple.
list = ["C" , "D" , "A" , "A" , "B" , "B" , "A"]
print(list.count("A"))

# Store the above values in a list & sort them from “A” to “D”
list = ["C" , "D" , "A" , "A" , "B" , "B" , "A"]
print(list.sort())
print(list)

# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
list = ["m" , "a" , "m"]
list_copy = list.copy()
list_copy.reverse()
if(list_copy == list):
    print("Palindrome")
else:
    print("Not Palindrome")