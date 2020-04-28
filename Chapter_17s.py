#--Functional Programming--

#--Lets start with a simple Object Oriented program 
#--we want to count the no. of lines in a file 

#--version 1 :
class LineCounter:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.lines = []
        self.count = 0

    def read(self):
        for line in self.file:
         self.lines.append(line)
         self.count += 1

        print(self.count) 
        print(self.lines) 

    
lc = LineCounter("suven/feed.txt")
lc.read()

#-------------
#--version 2
#-- Here we first read into a [] , then count. 

class LineCounter:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.lines = []

    def read(self):
        self.lines = [line for line in self.file]

    def count(self):
        return len(self.lines)

lc = LineCounter("suven/feed.txt")
lc.read()
print(lc.count()) 

#------
#--Pointers :
1> Here read() and count() are methods.
2> and lines[] is the property.
3> property values become the state of the object.
4> property values are manipulated by methods.
#------   

#--Rewriting the above code , with out class
#--Instead using only pure , independent functions

def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]

def count(lines):
    return len(lines)

example_lines = read('suven/feed.txt')
lines_count = count(example_lines)
print(lines_count)

#------
#--Refer notes for understanding difference between pure and impure functions.
#------

#-----The Lambda Expression
#------------------------------
#--Redefine this simple add function
# Using `def` (old way).
def old_add(a, b):
    return a + b


#--redefined in the new way as lambda expression 	
new_add = lambda a, b: a + b

print(new_add(10,5))

#--------------
#--map()  
#--# Pseudocode for map.
#--------------------
def map(func, seq):
    # Return `Map` object with
    # the function applied to every
    # element.
    return Map(
        func(x)
        for x in seq
    )
#---------------------
#--map() example: where we are adding some constant value to each member of the list. 

values = [1, 2, 3, 4, 5]

#-Note: We convert the returned map object to
# a list data structure.
add_10 = list(map(lambda x: x + 10, values))
add_20 = list(map(lambda x: x + 20, values))

print(add_10)

print(add_20)

#-----------------------

#--The Filter Function
#--Pseudocode for filter.
#--------------
def filter(evaluate, seq):
    # Return `Map` object with
    # the evaluate function applied to every
    # element.
    return Map(
        x for x in seq
        if evaluate(x) is True
    )
#---------------

#--we could filter odd or even values from a list:
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Note: We convert the returned filter object to
# a list data structure.
even = list(filter(lambda x: x % 2 == 0, values))
odd = list(filter(lambda x: x % 2 == 1, values))

print(even)

print(odd)

#----------------------------

#--The Reduce Function
from functools import reduce

values = [1, 2, 3, 4]

summed = reduce(lambda a, b: a + b, values)
print(summed)

#-------------------