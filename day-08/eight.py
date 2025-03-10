# File I/O in Python
# Python can be used to perform operations on a file. (read & write data , close ,open % delete)
# mtlb ham kisi bh file ko manupulate krskte hai by using python $ hamari at the end sari files 0 ,1 me hi store hoti hai 
# 1.Text Files : .txt, .docx, .log etc.
# 2.Binary Files : .jpeg, .png, .mov, .mp4

# Open, read & close File
# We have to open a file before reading or writing.
open("file name","mode")
f = open("demo.docx" ,"r" )
data = f.read()
print(data)
print(type(data))
f.close()

# Chracter & Meaning
# r   :  open for reading(by default)
# w   : open for writing, truncating the file first => mtlb pehel file ka data delete hoga phr write mtlb overwrite kr rahai hai & also create a new file
# x   : create a new file and open it for writing
# a   : open for writing , appending & also create a new file
# b   : binary mode
# t   : text mode(by default)
# +   : both for (reading and writing) => example : w+ = read bh or write bh

# Reading a File
# data = f.read() =>> read entire file
# data = f.readline() ==>> read one line at time
f = open("demo.docx","r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close()

# Writing to a File
x = open("demo.docx","w")
x.write("Python is indentation language")
x.close()

# a ==> append mean add more in file
x = open("demo.docx","a")
x.write("\nPython is implicit language")
x.close()

# r+ (ye starting me over write krta hai jitna write kia hai na utne hi letter overwrite hote hai)
f = open("sample.docx","r+")
f.write("abc")
f.close()

# w+ (ye bh read and write but ye completely file ko overwrite krdeta hai)
x = open("sapmle.docx","w+")
print(x.read())
x.write("Hello")
x.close()

# with new syntax( ye better way hai file ko read , write krne or jb with use kre to wo automatically file ko close bh krdeta hai)
with open("random.docx","w") as f:
    data = f.write("new data")
    print(data)

# Deleting a File : using the os module
# Module (like a code library) is a file written by another programmer that generally has a function we can use
import os
os.remove("random.docx")

# Lets Practice
# Create a new file “practice.txt” using python. Add the following data in it:
f = open("demo.docx","w")
data = f.write("Hi everyone\nwe are learning File I/O\nusing Python\nI like programmig in Python")
print(data)
f.close()

# WAF that replace all occurrences of “python” with “java” in above file.
with open("demo.docx","r") as f:
    data = f.read()
    print(data)
new_data = data.replace("Python","Java")
print(new_data)
with open("demo.docx","w") as f:
    f.write(new_data)

# Search if the word “learning” exists in the file or not.
word = "learning"
with open("demo.docx","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Not Found")