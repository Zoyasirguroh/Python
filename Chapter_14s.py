#--Inheritance, Overloading and Overriding
#--------------------------------------------------------
#--Employee is the super-class and GovtServant is a sub-class
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


class GovtServant(Employee):
    'this is the subclass inheriting from employee superclass'
    def __init__(self, name, salary, dept, areaCode):
      Employee.__init__(self, name, salary)
      self.dept = dept
      self.areaCode = areaCode
      
    def responsibleFor(self):
      print("Good Governance with no Corruption")

gs = GovtServant("Modi Ji", 1000000, "Central Govt", "Full India")
gs.displayCount()
gs.displayEmployee()
gs.responsibleFor()
	
#---------------------------------------------

#--we can keep the child class empty, like this :
class Parent(object):
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class Child(Parent):
    pass  #pass is keyword to route all calls to super methods
	
c = Child()
print(c.get_value())

#--Error 1: See running the code without "pass" k/word 

#--Note 1: get_value() is not a method of child-class
#-- to check this, run the below code 
class Parent(object):
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class Child(Parent):
    pass  #pass is keyword to route all calls to super methods
	
print("See Parent class name-space \n\n", Parent.__dict__)
print("-----------------------------------")
print("See Child class name-space \n\n", Child.__dict__)
print("-----------------------------------")

#--Note 2: Now if we re-define that is Override the method:
#--the Child class actually contains a get_value() method with a different implementation (the id of the two functions are different).

class Parent(object):
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class Child(Parent):
    def get_value(self):
        return self.value+1
	
print("See Parent class name-space \n\n", Parent.__dict__)
print("-----------------------------------")
print("See Child class name-space \n\n", Child.__dict__)
print("-----------------------------------")


#---------------------------------------------

#--example using issubclass() and isinstance()

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


class GovtServant(Employee):
    'this is the subclass inheriting from employee superclass'
    def __init__(self, name, salary, dept, areaCode):
      Employee.__init__(self, name, salary)
      self.dept = dept
      self.areaCode = areaCode
      
    def responsibleFor(self):
      print("Good Governance with no Corruption")

gs = GovtServant("Modi Ji", 1000000, "Central Govt", "Full India")
print("is Govt-Servant subclass to Employee ", issubclass(GovtServant, Employee))
print("is gs object of Employee ", issubclass(GovtServant, Employee))
print("Is gs instance of Govt-Servant", isinstance(gs, GovtServant))
print("Is gs instance of Employee", isinstance(gs, Employee))

class Student :
  def __init__(self, name):
   self.name = name
  
print("Is gs instance of Student", isinstance(gs, Student))
   
#---------------------------------------   
     
#-- Simple Example to show Overriding :
class Parent:        # define parent class
   def myMethod(self):
      print ('Calling parent method')

class Child(Parent): # define child class
   def myMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.myMethod()         # child calls overridden method

#----------------------------------------

#--Meaningful example of Overriding
import datetime

class Logger(object):
    def log(self, message):
        print(message)

class TimestampLogger(Logger):
    def log(self, message):
        message = "{ts} {msg}".format(ts=datetime.datetime.now().isoformat(), msg=message)
		
        super().log(message)

		
#--The TimestampLogger object adds some information to the message string before calling the original implementation of its log() method.		
l = Logger()
l.log('hi!')
print("----------------------------")
t = TimestampLogger()
t.log('hi!')

#--Good practice : Call the original implementation of a method you are overriding whenever possible.		 

#-----------------------------------------------
#--Coding Exercise 
#--Extend the class FileReading to define a class FileReadingWithNoBlankLines. Complete your code as below.
#--Hint : use strip() to strip out the blank lines. 


import os
 
class FileReading:
    def cat(self, filepath):
        f = open(filepath)
        lines = f.readlines()
        f.close()
        return lines

class FileReadingWithNoBlankLines(FileReading):
    def cat (self, filepath):
        lines=super().cat(filepath)
        non_blank_count=0
        
        for line in lines:
            if line.strip():
                non_blank_count+=1
        return non_blank_count
        
count_with_blank_lines = FileReading()
countb = count_with_blank_lines.cat("suven/linkedin_comments.txt")

print(len(countb)) #count of lines 

print("-----------------------------")

count_without_blank_lines = FileReadingWithNoBlankLines()
count_no_b = count_without_blank_lines.cat("suven/linkedin_comments.txt")

print(count_no_b) #count of non-blank lines


#--About the above prg :
#-----------------------------------------------
1> super class FileReading, opens a file, reads all lines and returns a list.
2> sub class FileReadingWithNoBlankLines, calls the super class to get the lines, then we use strip() to avoid the blank lines.
#-- strip() returns true for a non-blank line.
#-- for blank lines it returns false

#-----------------------------------------------


#--Method Overloading 
#------------------------------------
#---example of method Overloading----

class Human:
 def sayHello(self, name=None):
 
  if name is not None:
   print('Hello ', name)
  else:
   print('Hello ')
 
#Create instance
obj = Human()
 
#Call the method
obj.sayHello()
 
#Call the method with a parameter
obj.sayHello('Suven')

#--------------------------------------
#---Be careful don't override like this : 
#-- See Error :
class A:
    def stackoverflow(self):    
        print('first method')
    def stackoverflow(self, i):
        print('second method', i)

ob=A()
ob.stackoverflow(2)
ob.stackoverflow()
#this program isa case of  method hiding only the last method works
#-------------------------------------
#--Coding Exercise : Correctly override above stackoverflow() 
#-- in 2 ways.
 
#--correct way of Overloading is : 
class A:
    def stackoverflow(self, i=None):    
        if i is None:
            print('first method')
        else:
            print('second method')
ob=A()
ob.stackoverflow(2)
ob.stackoverflow()

####------ or like this --------
class A:  

        #-- your code here --
			
ob=A()
ob.stackoverflow(2)
ob.stackoverflow()			


#----------------------------

#--Method & Operator Overloading  
#--many built-in operators are overloaded by overloading some magic methods , for e.g :
#same operator behaves differently with change of operands i.e parameters, see OL1

#--example : OL1
#Adds the two numbers
print(1 + 2)

#Concatenates the two strings
print('Learning' + 'Python')

#Gives the product
print(3 * 2)

#Repeats the string
print('Python' * 3)

#----------------------------------------------

#--overloading the special or magic or dunder methods or
#--Overloading Built-in Functions
#--example : OL2

class Order:
  def __init__(self, cart, customer):
   self.cart = list(cart)
   self.customer = customer

  def __len__(self):
    return(len(self.cart))
order = Order(['marker', 'red-pen', 'pencils'], 'SCTPL')

print(len(order)) #finds len of the cart of items

#--------------------------------

#--example : OL3
#--__str__() and __repr__() both are used to represent the object as string. If we don't override this method, then it prints address of the object. 

class Vector:
  def __init__(self, x_comp, y_comp):
   self.x_comp = x_comp
   self.y_comp = y_comp

  def __repr__(self):
   return f'Vector({self.x_comp},{self.y_comp}),x'
   
  def __str__(self):
   return f'Vector({self.x_comp},{self.y_comp}),y'
   
   
v = Vector(3,5)

#print(str(v)) #calls the overridden str()
print (v)
#print(repr(v)) #calls the overridden repr()

#note by default __str__ fuction is called

#---------------------------

#--Making Your Objects True or False by overloading bool()
#--in below code : "if" checks the bool status
class Order:
 def __init__(self, cart, customer):
  self.cart = list(cart)
  self.customer = customer

 def __bool__(self):
  return len(self.cart) > 0

order1 = Order(['Mobile', 'headphones', 'case-covers'], 'ABC')
order2 = Order([], 'XYZ')

for order in [order1, order2]:
 if order:
  print(f"{order.customer}'s order is processing...")
 else:
  print(f"Empty order for customer {order.customer}")

#------------------------------------

#--example : OL4 : 
#--Making Your Objects Capable of Being Added Using +
class Order:
 def __init__(self, cart, customer):
  self.cart = list(cart)
  self.customer = customer

 def __add__(self, other):
  new_cart=self.cart.copy()
  new_cart.append(other)
  return Order(new_cart, self.customer)
  

order = Order(['OnePlus', 'MobileCover'], 'ABC')
print(order.cart)

order = order + 'amazon'  
print(order.cart)
#------------------------------- 
Similarly , we can overload __sub__(), __mul__() also
#-------------------------------
#--Project : Build a inheritance tree of primary logical gates. 
#--Lets look at complete inheritance example
#--Build a inheritance tree having the following :
# top level class : Logic Gate
# second level class : Binary Gate and Unary Gate
# last level class : 
#--Under Binary : And , OR Gate
#--Under Unary : Not Gate
#-------------------------------

#--Version 1: 
class LogicGate:

    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
		
#--not coded : performGateLogic()
#--will code it in the sub-class
#--the GateLogic of OR , AND , NOT would be different		

#-----------------------------------------

class LogicGate:

    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
		
#--not coded : performGateLogic()
#--will code it in the sub-class
#--the GateLogic of OR , AND , NOT would be different

class BinaryGate(LogicGate):

    #--your code here


class UnaryGate(LogicGate):

    #--your code here
	

		
class AndGate(BinaryGate):

    #--your code here
	
	

class OrGate(BinaryGate):

    #--your code here
	
	

class NotGate(UnaryGate):

    #--your code here
	
	


#Lets try all the gates
g1 = AndGate("G1")
print("for And gate :", g1.getOutput())
print("-------------------------------")
g2 = OrGate("G2")
print("for OR gate :", g2.getOutput())
print("-------------------------------")
g3 = NotGate("G3")
print("for NOT gate :",g3.getOutput())
#-------------------------------------------------
#-------------------------------------------------
#program we coded in lec
class LogicGate:
    
    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.PinA = None
        self.PinB = None
    def getPinA(self):
        return int(input("Enter pin A input for gate"+self.getLabel()+"--->"))
    def getPinB(self):
        return int(input("Enter pin B input for gate"+self.getLabel()+"--->"))


class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.Pin = None
    def getPin(self):
        return int(input("Enter pin  input for gate"+self.getLabel()+"--->"))   

class AndGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)
    def performGateLogic(self):
        a=self.getPinA()
        b=self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)
    def performGateLogic(self):
        a=self.getPinA()
        b=self.getPinB()
        if a==1 or b==1:
            return 1
        else:
            return 0


class NotGate(UnaryGate):
    def __init__(self,n):
        UnaryGate.__init__(self,n)
    def performGateLogic(self):
        a=self.getPin()
        if a==1:
            return 0
        else :
            return 1

#Lets try all the gates
g1 = AndGate("G1")
print("for And gate :", g1.getOutput())
print("-------------------------------")
g2 = OrGate("G2")
print("for OR gate :", g2.getOutput())
print("-------------------------------")
g3 = NotGate("G3")
print("for NOT gate :",g3.getOutput())
#-------------------------------------------------
#-------------------------------------------------


#-------------------------------------------------			   
#---- multiple Inheritance
#------------------------------------------ 
class derive-class(<base class 1>, <base class 2>, ..... <base class n>):  
    <class - suite>   
#------------------------------------------	
	
#--example of multiple Inheritance	
class clock:
  """ code of a clock which ticks ahead every second """
  
class calender:
  """ code of a calender which shows today's date """

class calenderClock(clock, calender):
  """ derives property of both """

#---------------------------------------

#--a very simple implementation example--   
class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  

class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  

class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  

d = Derived()  
print(d.Summation(10,20))  
print(d.Multiplication(10,20))  
print(d.Divide(10,20))  

#--------------------------------------
#--Coding Exercise 4 :
#--in multiple inheritance : be careful of 
#--The Diamond Problem

class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")
    
class C(A):
    def m(self):
        print("m of C called")

class D(B,C):
    pass

x = D()
x.m()
#--see the o/p parameter
#--An object of sub-sub-class would always call methods of first inheriting class in case of overridden methods

#-----------------------------------------
#--Coding Exercise 5 :
# q> Whats the o/p of this ?
class A:
    def m(self):
        print("m of A called")

class B(A):
    pass
    
class C(A):
    def m(self):
        print("m of C called")

class D(B,C):
    pass

x = D()
x.m()

#--------------------
#--Coding Exercise 6
#--calling method m() from all classes 

class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")
    
class C(A):
    def m(self):
        print("m of C called")

class D(B,C):
    def m(self):
        print("m of D called")

#-- making object of sub-sub-class
x = D()

B.m(x) #have to pass some object. self needs some object
C.m(x) #please note you are calling via class-name 
x.m() #note you are calling via object now. Hence self gets reference of x

#--once again calling m()
x1 = B()

B.m(x1) #have to pass some object
C.m(x1)
x1.m()
#priority must be given to the call class
#--self gets some reference. Although we are not using it.
 
#-----------
#--Self Try out code 
#--using self reference in the above example
class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        if isinstance(self, B) : 
         print("m of B called")
        else :
         print("m of some one else called")
         print("m of ", self, "called")
		 
class C(A):
    def m(self):
        print("m of C called")

class D(B,C):
    def m(self):
        print("m of D called")

#-- making object of sub-sub-class
x = A()

B.m(x) 

#-- now call m() without any parameter
x1 = B() 
B.m(x1)

#-------------------------------------

		

