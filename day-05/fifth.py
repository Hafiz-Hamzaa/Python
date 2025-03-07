# Dictionary & Sets 
# Dictionary in Python:Dictionaries are used to store data values in key:value pairs
# They are unordered, mutable(changeable) & don’t allow duplicate keys
dict = {
    "name" : "Hamza",
    "age" : 23,
    "cgpa" : 3.4
}
print(dict)
print(dict["name"]) # access value through key
dict["name"] = "Ali" # updated or changeable
print(dict)
dict["lang"] = "English" # add new dictionary
print(dict)

# Nested Dictionaries
info = {
    "name" : "Amna",
    "marks" : {
        "math" : 80,
        "urdu" : 70,
        "computer" : 75
    }
}
print(info)
print(info["marks"])
print(info["marks"]["computer"])

# Dictionary Methods
# myDict.keys( ) returns all keys
student = {
    "name" : "umer",
    "age" : 20,
    "prof" : "designer"
}
print(student.keys())
print(list(student.keys())) # simply we can covert ito list by tupe casting

# myDict.values( ) returns all values
print(list(student.values()))

# myDict.items( ) returns all (key, val) pairs as tuples
print(list(student.items()))

# myDict.get( “key““ ) return the key according to value
# dono way same result degai but there is a differnce between gr hamne koi aisi key access krni chahe lekin wo exist hi nh krti to normal wala tareea hai square bracket wala usme error ajai ga OR agr hamen get method se access ki lekin usme error nh None aiga
print(student["prof"])
print(student.get("prof"))

# myDict.update( newDict ) inserts the specified items to the dictionary
student.update({"name": "mubashir"})
print(student)

# Set in Python
# Set is the collection of the unordered items.
# Each element in the set must be unique & immutable.
nums = {1 , 2 , 3 , 4}
print(nums)
print(len(nums))
print(type(nums))

# #repeated elements stored only once
# qkai python duplicate values ko ignore krdeta hai isliye value hamesha set me unique hoti hai
set2 = {1 , 2 , 2 , "hello" , "world" , "world"}
print(set2)

# empty set
empty_set = {} # ye empty dictionary hai set nh
print(type(empty_set))
# ye right syntax hai empty set ka
empty_set = set()
print(type(empty_set))

# Set Methods
# set jo hai wo mutable hota yad rkhna lekin jo set kai elements hote hai wo immutable hote hai qkai wo unique hota hai
set = {1 , 2 , 3 , 4}
# set.add( el ) adds an element
set.add(5)
# set.remove( el ) removes the elem an
set.remove(1)
print(set)

# set.clear( ) empties the set
set = {"hello" , "world" , "program"}
print(len(set)) # 3
set.clear()
print(len(set)) # 0

# set.pop( ) removes a random value
set = {"cake" , "biscuit" , "mango" , "apple"}
set.pop()
print(set)

# set.union( set2 ) combines both set values & returns new
set1 = {1 , 2 , 3}
set2 = {3 , 4 , 5}
result = set1.union(set2)
print(result)

# set.intersection( set2 ) combines common values & returns new
set1 = {1 , 2 , 3}
set2 = {3 , 4 , 5 , 2}
result = set1.intersection(set2)
print(result)

# Practice Set
# Store following word meanings in a python dictionary :
dict = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture","list of fact and figures"]
}
print(dict)

# You are given a list of subjects for students. Assume one classroom is required for 1 subject.
#How many classrooms are needed by all students.
subjects = {"python" , "java" , "C++" , "python" , "javascript" , "python" , "javascript" , "C"}
print(len(subjects))

# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.
dict = {}
marks1 = int(input("Enter marks of math subj : "))
marks2 = int(input("Enter marks of urdu subj : "))
marks3 = int(input("Enter marks of computer subj : "))
dict.update({"math" : marks1})
dict.update({"urdu" : marks2})
dict.update({"computer" : marks3})
print(dict)

# Figure out a way to store 9 & 9.0 as separate values in the set.
values = {"9.0" , 9} # first way
print(values)
values = {
    ("int" , 9),
    ("float" , 9.0)
}
print(values) # second way