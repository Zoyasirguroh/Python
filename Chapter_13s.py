#--Creating Classes
#-- Syntax : 
class ClassName:
   'Optional class documentation string'
   class_suite
   
#--The class has a documentation string, which can be accessed via ClassName.__doc__.

#--The class_suite consists of all the component statements defining class members, data attributes and functions.
#--------------------------------------------------------
#-- example : 1
class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)
	  
#--This would create first object of Employee class
emp1 = Employee("Neetu", 23000)

#--This would create second object of Employee class
emp2 = Employee("Vipin", 25000)

#--calling instance methods
emp1.displayEmployee()
print("-----------------------")
emp2.displayEmployee()
print("-----------------------")
#--calling class method
emp1.displayCount()

#---------------------------------------
#-- very important concept
#-- use of self 
class SomeClass:
    def __init__(self):
        self.arr = [] 
            
    def insert_to_arr(self, value):
        self.arr.append(value)

obj1 = SomeClass()
obj2 = SomeClass()
obj1.insert_to_arr(6)

here we have created obj1 and are calling the instance method insert_to_arr() of SomeClass while passing an argument 6. But now how does that method know "which object is calling me and whose instance attributes should be updated". 

Ans : self gets refr to obj1

#---------------------------------------
#--Instead of directly accessing attributes, use the following functions---------------------
getattr(obj, name[, default]) 
hasattr(obj,name)
setattr(obj,name,value) 
delattr(obj, name)
#---------------------------------------
#-- example : 2
class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      self.loc = None
      Employee.empCount += 1
   
   def displayCount(self):
     print("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)
      print("location is : ", self.loc)

print("------------------------")	  
#--This would create first object of Employee class
emp1 = Employee("Neetu", 23000)
emp1.displayEmployee()
print("-----------------------------------")

print(getattr(emp1, "salary", 10000))
print(getattr(emp1, "sal", 10000)) #see default value o/p
print(hasattr(emp1,"salary"))

#--change the value of salary attribute. 
#--setters have no return value
setattr(emp1,"salary","24500")

print("See new Sal : ", getattr(emp1, "salary", 10000))

#--deleting a un-wanted attribute
print("deleting location attribute :",delattr(emp1, "loc"))

#----------------------------------

#-- for defn class method use annotation
class SomeClass:
    def create_arr(self): # An instance method
        self.arr = []
    
    def insert_to_arr(self, value):  #An instance method
        self.arr.append(value)
        
    @classmethod
    def class_method(cls):
        print("the class method was called")
		
# we are calling the class method, not instance method 
SomeClass.class_method()  		
# Note: that the class calling becomes the parameter : cls


#----------------------------------
#--Built-In Class Attributes
#-- example : 3
class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

emp1 = Employee("Neethu", 23000)
emp2 = Employee("Vipin", 25000)
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__ )

#----------------------------------------------

#--Class Inheritance
#--Syntax :
class SubClassName (ParentClass1[, ParentClass2, ...]):
   'Optional class documentation string'
   class_suite
#----------------------------------------------

#--example 4: of a single inheritance
class Super:        # define parent class
   superAttr = 300
   def __init__(self):
      print("Calling Super constructor")

   def superMethod(self):
      print('Calling Super method')

   def setAttr(self, attr):
      Super.superAttr = attr

   def getAttr(self):
      print("Parent attribute :", Super.superAttr)

class Child(Super):     # define child class
   def __init__(self):
      print("Calling child constructor")

   def childMethod(self):
      print('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.superMethod()     # calls parent's method
c.setAttr(210)       # again call parent's method
c.getAttr()          # again call parent's method

#----------------------------------------------
#---Overriding Methods
#-- very simple example 

class Parent:        # define parent class
   def dummy(self):
      print('Calling parent method')

class Child(Parent): # define child class
   def dummy(self):
      print('Calling child method')

c = Child()          # instance of child
c.dummy()         # child calls overridden method


#-----------------------------------------------
#--Case Study : 
#--Implement the abstract data type "Fraction" e.g.: 2/7
#--version 1: 
class Fraction:

    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

myfraction = Fraction(2,7)

#--if you print the object of Fraction class
print(myfraction)
#--it prints moduleName.className at <addr>
#--object always prints its address


#--version 2:
#--adding methods to print the object as string
class Fraction:
    def __init__(self,top,bottom):
     self.num = top
     self.den = bottom
	 
    def show(self):
     print(self.num,"/",self.den)

    def __str__(self):
     return str(self.num) + "/" + str(self.den)
		
myfraction = Fraction(2,5)

#--call the show()
myfraction.show()

#--print the object directly. It calls __str__ method
print(myfraction)

#--version 3.a:
#--check whether the fraction objects are equal or not
#--this code checks object references only
class Fraction:
     def __init__(self,top,bottom):
         self.num = top
         self.den = bottom

     def __str__(self):
         return str(self.num)+"/"+str(self.den)

x = Fraction(1,3)
y = Fraction(1,3)
print(x == y) #shallow comparison or shallow equality


#--version 3.b:
#--this code checks object contents i.e Deep comparison
#--overload __eq__ method
class Fraction:
     def __init__(self,top,bottom):
         self.num = top
         self.den = bottom

     def __str__(self):
         return str(self.num)+"/"+str(self.den)
     
     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum == secondnum


x = Fraction(1,3)
y = Fraction(1,3)
print(x == y)



#--version 4:
#--overload the built-in method __add__ to add 2 fractions
 class Fraction:
     def __init__(self,top,bottom):
         self.num = top
         self.den = bottom

     def __str__(self):
         return str(self.num)+"/"+str(self.den)
     
     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum == secondnum
     
     def __add__(self, otherfraction):
        newnum= self.num * otherfraction.den+otherfraction.num * self.den
        newden=self.den*otherfraction.den
        
        return Fraction(newnum, newden)


f_one = Fraction(1,4)
f_two = Fraction(1,2)

f_three= f_one + f_two

print(f_three)
 
#--your code here



#--version 5: 
#--after adding the fractions, the result should be shown in reduced form

def gcd(m, n):
    while m % n !=0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n



class Fraction:
     def __init__(self,top,bottom):
         self.num = top
         self.den = bottom

     def __str__(self):
         return str(self.num)+"/"+str(self.den)
     
     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum == secondnum
     
     def __add__(self, otherfraction):
        newnum= self.num * otherfraction.den+otherfraction.num * self.den
        newden=self.den*otherfraction.den
        common=gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)


x= Fraction(1,4)
y= Fraction(1,2)



print(x+y)



class Fraction:
     def __init__(self,top,bottom):
         self.num = top
         self.den = bottom

     def __str__(self):
         return str(self.num)+"/"+str(self.den)

     def show(self):
         print(self.num,"/",self.den)

     def __add__(self,otherfraction):
         #--your code here
		 
x = Fraction(1,2)
y = Fraction(2,3)
print(x+y)
print(x == y)
 



#------------------------------------------------
#--Another case Study 
#--Overloading Operators
#--many a times we overload the 4 basic operators +,-,*,/
#--example 6:

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self,other):
        return Vector (self.a + other.a, self.b + other.b)
    
    def __sub__(self,other):
        return Vector (self.a - other.a, self.b-other.b)
    
    def __mul__(self,other):
        return Vector (self.a * other.a, self.b * other.b)
    
    def __truediv__(self,other):
        return Vector (self.a // other.a, self.b // other.b)

 
v1 = Vector(2,10)
v2 = Vector(5,-2)
print("Addition : ", v1 + v2)
print("Subtraction : ", v1 - v2)
print("Multiplication : ", v1 * v2)
print("Division : ", v1/v2)
 

#-----------------------------------------------
#--Data Hiding
#--------------------------
class MyPincode:
   __secretPincode = 400074
  
   def increment(self):
      self.__secretPincode += 1
      print(self.__secretPincode)

pin = MyPincode()
pin.increment()
pin.increment()
print("---------------------------")
#--------see the error---------
print(pin.__secretPincode)
print("---------------------------")

#this will work Object._Classname__secretData
#print(pin._MyPincode__secretPincode)


#-----------------------------------------------
#--Destroying Objects (Garbage Collection)--

class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
	  
   def __del__(self):
      class_name = self.__class__.__name__
      print(class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1

#prints the ids of the objects
print (id(pt1), id(pt2), id(pt3))  
del pt1
del pt2
del pt3

#------------------------------------------