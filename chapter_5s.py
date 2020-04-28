#--file basics--
#--Opening and Closing Files--
#--Before you can read or write a file, you have to open it using Python's built-in open() function.
#--syntax of open()
file object = open(file_name [, access_mode][, buffering])

#--If the buffering value is set to 0, no buffering takes place. 
#--If the buffering value is 1, line buffering is performed while accessing a file. 

#-syntax of close()
fileObject.close();

#--file Object Attributes
#-1> file.closed  
#-2> file.mode
#-3> file.name

#-example prg 
fptr = open("suven/test.txt", "rb")
print("Name of the file: ", fptr.name)
print("Closed or not : ", fptr.closed)
print("Opening mode : ", fptr.mode)
fptr.close()


#--Reading and Writing Files
#-for reading use fileObject.read([count]);    
#-for writing fileObject.write(string);

#-- program to r/w --
fptr = open("test.txt", "w")
fptr.write("Python is a \ngreat language")
fptr.close()

#opening again but in a different mode
fptr = open("suven/test.txt", "r+")
str = fptr.read(100) #read up to 100 chars
print("Read String is : ", str)
fptr.close()

print("---------------------------------")

#can open r/w mode also , like this
fptr = open("test.txt", "r+") #can use w+ also   
fptr.write("first:I am writing.\nthen:I will read")
fptr.seek(0)#reset the ptr to start of file
str = fptr.read(100)
print("Read String is : ", str)
fptr.close()

#----File Positions---
#Opens a file
fptr = open("test.txt", "r+")
str = fptr.read(10)
print("Read String is : ", str)

#Check current position
position = fptr.tell()
print("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fptr.seek(0, 0)
str = fptr.read(10)
print ("Again read String is : ", str)
fptr.close()

#---------------
#read from a file. Take file name as input
#on running : suven/test.txt   --> specify full path

from sys import argv
script, filename = argv #unpacking

txt = open(filename)
print(f"Here's your file {filename}:")
print(txt.read())
txt.close()

print("-------------------")

print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again) 
print(txt_again.read())
txt_again.close()

#--------------
_____#----->Home assignment<------#
#--Reading and Writing Files--
from sys import argv
script, filename = argv
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')#w opens in overwrite mode.

print("Truncating the file. Goodbye!")
target.truncate()#this is optional in case of write mode.

print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1 + "\n")
#target.write() #needs exactly one parameter. 0 given
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print("And finally, we close it.")
target.close()


#-------------------
#--  Coding Exercise 1 : 
#--- Script to copy from one file to another----

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#-- your code goes here 


from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file=open(from_file)
indata = in_file.read()

print(f"the input file is {len(indata)} bytes long")

print(f"does the o/p file exist? {exists(to_file)}")
print(f"Ready, hit RETURN to continue, ctrl+c to abort.")
input()

out_file=open(to_file,'w')
out_file.write(indata)

print("alright, all done.")





#-----------
#--Complete the missing lines of code : 
#--Define functions to read from a file -- 
from sys import argv
script, input_file = argv

def print_all(f):
 #--print full file contents


def rewind(f):
 #--reset fptr to 0


def print_a_line(line_count, f):
 print(line_count, f.readline()) #line_count is dummy Var

#--open a file

print("First let's print the whole file:\n")

#--call print_all

print("Now let's rewind, i.e go to start of file.")

rewind(current_file) #goes to start of file

print("Let's print three lines:")

current_line = 5
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

#-----------

#---Renaming and Deleting Files--
import os

# Rename a file from test1.txt to test2.txt
os.rename("test1.txt", "test2.txt")


#------ removing files
import os
from os.path import exists

#delete a file
filename = "suven/test2.txt"
os.remove(filename)
print("test2.txt existence :", exists(filename))
#what if I delete a file, which does not Exist ?
os.remove(filename) #FileNotFoundError


#----Directories in Python
#-1> mkdir() Method
#-2> chdir() Method
#-3> getcwd() Method
#-4> rmdir() Method. 
##--Before removing a directory, all the contents in it should be removed.

#--example program--  
import os
from os.path import exists

# Create a directory "test"
#-- your code here ---
 import os
from os.path import exists

# Create a directory "test"
folderName = "test123"
flag = exists(folderName)
if not flag :
 dir_ptr = os.mkdir(folderName)
 #creating a file inside a directory
#-- your code here ---
print("I will create a file, give me filename:")
filename=input("> ")
fullpath= folderName + "\\" + filename;
print("this is the path ", fullpath)
fptr = open(fullpath,'w+')
fptr.write("some dummy text")
fptr.close()




#--version 2 of the above prg
#--another way to change path
import os
from os.path import exists

# Create a directory "test"
folderName = "test123"
flag = exists(folderName)
if not flag :
 dir_ptr = os.mkdir(folderName)
 
#lets change to new directory
#-- your code here ---
newpath=os.chdir(folderName)
print(os.getcwd())


#creating a file inside new directory
#-- your code here ---

print("I will create a file, give me filename:")
filename=input("> ")

#fullpath = folderName + "\\" + filename;
#print("this is the path ", fullpath)

fptr = open(filename, 'w+') 
fptr.write("some dummy text")
fptr.close()



#--mini file project
#--Create a simple invoicing program, which should:
1> Help keep track of purchases people made from me. 
2> Search the invoice file for a keyword (the invoice number) 
3> Lets you enter a new invoice to a file named inv.txt
#------------

#Invoice Entering Program for EnY


print("EnY Invoice Program\n")
look_in = "suven\inv.txt"

while True:
 file = input("Enter 0 to Quit. Enter S to Search The File. Press ENTER to Input new Entries *Case Sensitive*: " )
 
 #-- your code here ---
 if file=="0":
    print("exiting program")
    break 
 elif file=="S":
    keyword=input("enter invoice number to search: ")
    with open(look_in,"r") as search_file:
        for line in search_file:
         if keyword in line:
          print(line)
 else:
    NAME= input("enter Customer name : ")  
    innum=input("enter invoice number: ")
    quant=int(input("enter Quantity : "))    
    price=quant* 500
    with open(look_in,"at") as out_file:
      out_file.write("Name:%s || invoice number:%s ||quant:%s||. price:%s"%(NAME, innum, quant,price))
 
 
 
 
 
 
#-------------------

#--use with keyword when dealing with file streams--
The with statement simplifies exception handling by encapsulating common preparation and cleanup tasks in so-called context managers. 

For instance, the open statement is a context manager in itself, which lets you open a file, keep it open as long as the execution is in the context of the with statement where you used it, and close it as soon as you leave the context, no matter whether you have left it because of an exception or during regular control flow. Hence resource acquired by the with statement is released when you leave the with context.
 
#--------------------

#--re-coding the Invoice program to r/w from csv file

#Invoice Entering Program using CSV
import csv
print("EnY Invoice Program\n")
look_in = "suven\inv.txt"
template = "Name: {name} || Invoice Number: {invoice} || Quantity: {quantity} || Price: ${price}\n\n"

while True:
 file = input("Enter 0 to Quit. Enter S to Search The File. Press ENTER to Input new Entries *Case Sensitive*: " )
 
 if file=="0":
  print("Exiting Program...")
  break
 elif file=="S":
  keyword = input("Enter Invoice Number to Search: ")
  
  #-- your code here ---
  
  
  

#-----------