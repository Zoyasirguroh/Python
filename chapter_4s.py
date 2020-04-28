#-Functions , Modules & Packages

#--Functions
#-syntax of function
def functionname( parameters ):
   "function_docstring is optional"  
   function_suite
   return [expression]

#--example : 1 
# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return

# Now you can call printme function
printme("This is first call to the user defined function!")
printme("Again second call to the same function")


#--Pass by Reference vs Value
# All parameters (arguments) in the Python language are passed by reference. 

def seeChanges( mylist ):
   "This changes a passed list into this function"
   print("Values before change: ", mylist)
   
   mylist[2]=50
   print("Values after change: ", mylist)
   return

mylist = [10,20,30]
seeChanges( mylist )
print("Values outside the function: ", mylist)


#--whats the answer for this ?
def findTheAns( mylist ):
   mylist = [1,2,3,4] 
   print("Values inside the function: ", mylist)
   return

mylist = [10,20,30]
findTheAns( mylist )
print ("Values outside the function: ", mylist) 


#--Function Arguments
#You can call a function by using the following types of formal arguments −

#1> Required arguments
#2> Keyword arguments
#3> Default arguments
#4> Variable-length arguments

#1> Required arguments : example as above

#2> Keyword arguments
def printinfo(company, url):
   print("Company Name: ", company)
   print("URL ", url)
   return

# Now you can call printinfo function
printinfo( url = 'https://suvenconsultants.com', 
           company = "Suven Consultants" )


#3> Default arguments
		   

#--3> Rule : Default arguments always at last.
#--see the Error !!
def printinfo(company ="SCTPL",url):
   print("Company Name: ", company)
   print("URL ", url)
   return

# Now you can call printinfo function
printinfo( url = 'https://suvenconsultants.com')


#4> Variable-length arguments -> use pointers as in C
#syntax : 
def functionname([formal_args,] *var_args_tuple ):
   "function_docstring"
   function_suite
   return [expression]



#--example of Variable-length arguments--

def printinfo( arg1, *vartuple ):
   print("Output is: ")
   print(arg1)
   
   for var in vartuple:
      print("--",var)
   return

# Now you can call printinfo function
printinfo(10) #no variable arguments
printinfo(70,60,50) #with 2 variable arguments

#use pointer notation -> * -> means accepting many inputs
def print_two(*args):
 arg1, arg2 = args
 print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
 print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
 print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
 print("I got nothing'.")

print_two("Rocky","Suven")
print_two_again("Suven","Consultants")
print_one("ML-DL")
print_none()


#------------------- 
#--Anonymous Functions
#--use the lambda keyword not the def keyword
#--syntax of lambda functions contains only a single statement, which is as follows −

lambda [arg1 [,arg2,.....argn]]:expression

#--code example 
sum = lambda arg1, arg2: arg1 + arg2

#Now you can call sum as a function
print("Value of total : ", sum(12,13))
print("Value of total : ", sum(30,20)) 		   


#--above lambda can also be written as
def sum( arg1, arg2 ):
   total = arg1 + arg2
   print("Inside the function : ", total)
   return total

total = sum(10,20)
print("Outside the function : ", total )


#--Scope of Variables
#1> Global variables
#2> Local variables

total = 0   # These are global variable.
gtotal = 0  

def sum(arg1, arg2):
   total = arg1 + arg2; # Here total is local variable.
   global gtotal  #for using global variables inside fn
   gtotal = total
   print("Inside the function local total : ", total)
   return total

# Now call sum function
sum(10, 20)
print("Outside the function total : ", total)
print("Outside the function gtotal : ", gtotal)
#--local variables can be accessed only inside the function in which they are declared.


#--------------
#--A module allows you to logically organize your Python code

#-put this code into firstModule.py 
def print_func(par):
   print("Hello : ", par)
   return

#import the above module, like this :
import firstModule
firstModule.print_func("EY")


#--The from...import Statement

# from statement lets you import specific attributes from a module into the current namespace. Syntax is

from modname import name1[, name2[, ... nameN]]
#-----------

#--importing fib() from fibonacci module  
from fibonacci import fib
list = fib(100)
print(list) 


#-from...import * Statement
#--It is also possible to import all the names from a module into the current namespace

#--this would also work
from fibonacci import *
list = fib(100)
print(list) 


#--Executing Modules as Scripts
#-- save below script to __main__.py only.


# running this code as __main__ module
# __main__ means the current script file
def fib(n): 
   result = []
   a, b = 0, 1
   while b < n:
      result.append(b)
      a, b = b, a + b
   return result

if __name__ == "__main__":
   f = fib(100)
   print(f) 

#--------------
#--Locating Modules
#--When you import a module, the Python interpreter searches for the module in the following sequences −

#--1> The current directory.

#--2>If the module not found, Python then searches each directory in the environment variable PYTHONPATH.

#--3>If all else fails, Python checks the default path.
import sys
print("default path is ", sys.path)


#------------------

#dir() Function
#-dir() built-in function returns a sorted list of strings containing the names defined by a module.
import math
content = dir(math)
print(content)


#--globals() and locals()
total = 0   # These are global variable.
gtotal = 0  

def test(arg1, arg2):
   total = 10 
   print("locals are ", locals())
   print("--------------------------")
   print("globals are ", globals())
   return total

# Now call sum function
test(10, 20)


#----------
#--Packages
#--A package is a hierarchical file directory structure that defines a single Python application environment that consists of modules and subpackages.

#-- Packages 
Packages are namespaces which contain multiple packages and modules themselves. They are simply directories, but with a twist.

Each package in Python is a directory which MUST contain a special file called __init__.py. This file can be empty, and it indicates that the directory it contains is a Python package, so it can be imported the same way a module can be imported.


#--steps :
1> make a folder recruitment
2> code some .py files in it
3> code a empty __init__.py file and place it in the package 
4> 2 ways to : use the package by writing 
#-- sctpl.py --
from recruitment import interview_prep
from recruitment import first_call

interview_prep.interviewprep()
first_call.firstcall()

#--another way : sctpl.py
#--Note : we must use the package prefix whenever we access the module

import recruitment.interview_prep
import recruitment.first_call

recruitment.interview_prep.interviewprep()
recruitment.first_call.firstcall()


#----------
#--be careful don't use *  , like this 
from recruitment import *  #this won't work
#Why ?
because recruitment is a package. not a module.
and * means load all classes, functions and variables of a module into the current script. 


#--don't confuse between importing from a package 
#--w.r.t importing from a module 
from draw import *  #here draw.py file looks like :
#--------
# draw.py
def draw_game():
    ...

def clear_screen(screen):
    ...
#--------
#-- hence * means importing all objects from a module
#--------
   
   
#-- U may get an error like :
ModuleNotFoundError : No module named "some-Name" found

#--Check for the following 
1> Your script(using the package) and your package/folder(being referenced) should be in the path. 

2> if some or all modules are in different path then you could do this : 
PYTHONPATH=/otherFolder python suven.py
#-This will execute suven.py, and will enable the script to load modules from the "otherFolder" directory as well as the local directory. 


#-----------------
#--Exploring built-in modules---
Two very important functions come in handy when exploring modules in Python - the dir() and help() functions.
#--ex:
>>> import urllib
>>> dir(urllib)
#-- to help
>>> help(urllib)


#---- Coding Exercise 1: ----
#-you will need to print an alphabetically sorted list of all functions in the re module, which contain the word "find"
import re

# Your code goes here





#-----------------
#--how to install packages ?
refer 
https://packaging.python.org/tutorials/installing-packages/
 
#Try-outs
python --version
pip
pip --version
python -m pip install --upgrade pip setuptools wheel

#------------------

#--Coding Exercise 2:  
#-- lets code a very basic calculator ---
#-- code 4 functions add, sub, mul and div --





#----------------------