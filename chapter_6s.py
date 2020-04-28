#--Assertions & Exceptions

#----Assertions
Programmers often place assertions at the start of a function to check for valid input, and after a function 
call to check for valid output.
#---------------
#--Syntax
assert Expression[, Arguments]
#---------------

def KelvinToFahrenheit(Temperature):
   assert(Temperature >= 0),"Colder than absolute zero!"
   return((Temperature-273)*1.8)+32

print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
print(KelvinToFahrenheit(-5))

#--------------

#--Exceptions and handling them--

#--Syntax -------------
try:
   You do your operations here
   ......................
except Exception-1:
   If there is Exception-1, then execute this block.
except Exception-2:
   If there is Exception-2, then execute this block.
   ......................
else:
   If there is no exception then execute this block. 
#--------------

#---- run 2 cases -----
try:
   fptr = open("test.doc", "w")
   #fptr = open("test.doc", "r")
   fptr.write("This is my test file for exception handling!!")
except IOError:
   print("Error: can\'t find file or write data")
else:
   print("Written content in the file successfully")
   fptr.close()

#----------

#--The except Clause with No Exceptions--
try:
   You do your operations here
   ......................
except:
   If there is any exception, then execute this block.
   ......................
else:
   If there is no exception then execute this block. 
#---------------

#--The except Clause with Multiple Exceptions
try:
   You do your operations here
   ......................
except(Exception1[, Exception2[,...ExceptionN]]]):
   If there is any exception from the given exception list, 
   then execute this block.
   ......................
else:
   If there is no exception then execute this block. 
#--------------

#--The try-finally Clause
try:
   You do your operations here;
   ......................
   Due to any exception, this may be skipped.
finally:
   This would always be executed.
   ......................
#-----------------

#----Notes----- :
1> can provide except clause(s), or a finally clause, but not both. 
2> cannot use else clause along with a finally clause.
#--------------   

#--- run 2 test cases ---
try:
   fptr = open("test.txt", "w")
   try:
      fptr.write("This is my test file for exception handling!!")
   finally:
      print ("Going to close the file")
      fptr.close()
except IOError:
   print ("Error: can\'t find file")

#--------------

#--Argument of an Exception
try:
   You do your operations here
   ......................
except ExceptionType as Argument:
   You can print value of Argument here...
   
#------

def temp_convert(var):
   try:
      return int(var)
   except ValueError as Argument:
      print("The argument does not contain numbers\n", Argument)

ans = temp_convert("sctpl")
#ans = temp_convert(100)
print(ans)   

#------

#--Raising an Exception--
def functionName(level):
   if level<1:
      raise Exception(level)
   return level

try:
   l = functionName(-10)
   #l = functionName(10)
   print ("level = ",l)
except Exception as e:
   print("error in level argument",e.args[0])

#----------

#-- User-Defined Exceptions
Python also allows you to create your own exceptions by
deriving classes from the standard built-in exceptions.
#-----
would be seen when we learn classes & objects
#-----

#--------------------------------------
#--------------------------------------

#----Coding Assignment----
#--Read txt file and count lines, words and chars

fname = "suven\\feed.txt"
num_lines = 0
num_words = 0
num_chars = 0

#your code here....

with open(fname, 'r') as f:
    for line in f:
        words=line.split()
        
        num_lines+=1
        num_words+=len(words)
        num_chars+=len(line)
        
print ("No of lines in the ", fname, "is", num_lines)
print ("No of words in the ", fname, "is", num_words)
print ("No of chars in the ", fname, "is", num_chars)

#-------------------------------------

#-- Read txt file and get frequency of a keyword
fname = "suven\\feed.txt"

num_key_words = 0
print("enter the word to search")
key_word = input(">")

try:

#your code here....
try:
    with open(fname,'r') as f:
        for line in f:
            words=line.split()
            for word in words:
                if key_word in word:
                    num_key_words+=1
    print(num_key_words)
except IOError:
    print("Error: cant find file")
