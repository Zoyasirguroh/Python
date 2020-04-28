#--download Oracle from 
#--refer steps from db.suven.net
#--------------------------------------------------
#--install the package
pip install cx_Oracle
#--------------------------------------------------

#--example 1: try making connection
import cx_Oracle
con = cx_Oracle.connect('system', 'admin123', 'localhost:1521/XE')
print(con.version)
con.close()   

#--another way of making connection. Shorter notation 
import cx_Oracle
con1 = cx_Oracle.connect('system/admin123@localhost:1521/XE')
print(con1.version)
con1.close()   

#----- creating empdadar table:
create table empdadar (
empId int primary key,
empName varchar2(30) not null,
salary float not null,
dept varchar2 (30) not null,
designation varchar2(30)
);
insert into empdadar values(1, 'Batool', 35000, 'SALES','SALES_MNG');
insert into empdadar values(2, 'Zuhar', 37000, 'IT','DEVELOPER');
insert into empdadar values(3, 'Sana', 25000, 'support','Hr');
insert into empdadar values(4, 'nida', 25000, 'support','Hr');



#--fetch all records 
import cx_Oracle
con = cx_Oracle.connect('system/admin123@localhost:1521/XE')
cursor = con.cursor()
cursor.execute('SELECT * from employees_record')
print(cursor.fetchall())
con.close()   


#--try fetchmany() and fetchone()
import cx_Oracle
con = cx_Oracle.connect('system/admin123@localhost:1521/XE')
cursor = con.cursor()
cursor.execute('select * from empdadar')
print(cursor.fetchmany(2))
con.close()
#--your code here




#-------------------

#---to print records , column wise so that its easier to read.
#--use pprint() 
import cx_Oracle
from pprint import pprint
con = cx_Oracle.connect('system/admin123@localhost:1521/XE')
cursor = con.cursor()
cursor.execute('select * from empdadar')
pprint(cursor.fetchmany())
con.close()
#--your code here
 


#----------------------

#--Very important--
#--Cursor populates only when we first fetch records from it.

#----------------------


#--for example see this code :
import cx_Oracle
from pprint import pprint
con = cx_Oracle.connect('system/admin123@localhost:1521/XE')
cursor = con.cursor()
cursor.execute('SELECT * from employees_record')

print("No. of entries :", cursor.rowcount) #would print 0
print("---------------------------------------")

for row in cursor:
 print(row)

con.close()   

#-------------------------------

#--to get rowcount, as well print all records
import cx_Oracle
from pprint import pprint
con = cx_Oracle.connect('system/admin123@localhost:1521/XE')
cursor = con.cursor()
cursor.execute('SELECT * from employees_record')

res = cursor.fetchall();
print("No. of entries in :", len(res)) 
print("---------------------------------------")
pprint(res)

con.close()   

#--------------------------------
#--description attribute of cursor
#--access all column description info. of cursor objects
import cx_Oracle
from pprint import pprint
con = cx_Oracle.connect('system/admin123@localhost:1521/XE')
cursor = con.cursor()
cursor.execute('SELECT * from employees_record')

pprint(cursor.description)

con.close()   

#-------------------------------

#--using bind variables
import cx_Oracle
from pprint import pprint
con = cx_Oracle.connect('system/admin123@localhost:1521/XE')
cursor = con.cursor()
named_params = {'dept_id':100, 'sal':8000}
cursor.execute('SELECT * from employees_record where department_id=:dept_id and salary> :sal', named_params)

pprint(cursor.fetchall())
print("-------------------------------------")

#--another way
cursor.execute('SELECT * FROM employees_record WHERE department_id=:dept_id AND salary>:sal', dept_id=100, sal=8000)

pprint(cursor.fetchall())
print("-------------------------------------")

con.close()   

#-----------------------------------------------

#--use bindnames() method of the cursor to find bindings :
import cx_Oracle
from pprint import pprint
con = cx_Oracle.connect('system/admin123@localhost:1521/XE')
cursor = con.cursor()
named_params = {'dept_id':100, 'sal':8000}
cursor.execute('SELECT * from employees_record where department_id=:dept_id and salary> :sal', named_params)

#use the bindnames() method of the cursor to find bindings :

print(cursor.bindnames())

con.close()   

#----------------------------------------

#--giving bind parameters via position 
import cx_Oracle
from pprint import pprint
con = cx_Oracle.connect('system/admin123@localhost:1521/XE')
cursor = con.cursor()

positional_params = (100, 10000) #use tuple to give values

cursor.execute('SELECT * from employees_record where department_id= :1 and salary> :2', positional_params)

pprint(cursor.fetchall())

print("----------------------------")

#-----can also give direct values
cursor.execute('SELECT * from employees_record where department_id= :1 and salary> :2',(100, 10000))

pprint(cursor.fetchall())

con.close()   

#---------------------------------------------

#--Use preparedStatement
import cx_Oracle
from pprint import pprint
con = cx_Oracle.connect('system/admin123@localhost:1521/XE')
cursor = con.cursor()

positional_params = (100, 10000) #use tuple to give values

cursor.prepare('SELECT * from employees_record where department_id= :d')

#None->indicates I don't have a new query. Use preparedStatement
r = cursor.execute(None, {'d':100})

pprint(r.fetchall())

print("----------------------------")

con.close()
#Use or benefit of prepared Statement :
1> suppose u have a prg like this :
    a. asking for input from user 
    b.assigning bind var, say a and b
    c. using them in your select statement
    d. Above steps a-> c are put in a loop for 10000 times
2> By rule : Whenever a sql st, runs , 1st its syntax is checked . so due to the loop its syntax is checked for 10000 times . if each syntax checking waste 2msec of your time, then above code is not productive
3> Solution to the problem : Use Prepared Statement.
// for ex:
    cursor.prepare("select ......, : a, :b")
    cursor.execute(None, {a=x, b=y})
// in the loop we wud be asking the user to input us values for x and y

#-----------------
#--Coding Exercise : 3
#-- perform DDL : Create and Drop table
#-- create a table from python in Oracle

import cx_Oracle
from pprint import pprint
con = cx_Oracle.connect('system/admin123@localhost:1521/XE')
cursor = con.cursor()
sql="""create table professional1(
firstname  char(20) not null, 
lastname char(20),
age int, 
gender char(1),
income float )"""

cursor.execute(sql)
con.close()
#--Drop table if it already made.
#cursor.execute("DROP TABLE Professional")

# Create table as per requirement

#-- your code here --



#----------------------------

#--Coding Exercise : 4
#--Perform DML operations
#--Insert record in the above table 
import cx_Oracle
from pprint import pprint

con = cx_Oracle.connect('system', 'admin123', 'localhost:1521/XE')

cursor = con.cursor()
sql= ("""insert into professional1 (firstname  ,lastname ,age , gender ,income )values('zoya','khan', 22, 'F', 40000)""")

try:
    cursor.execute(sql)
    con.commit()
except:
    con.rollback()
con.close()

#-- your code here


#---------------------------------
#----insert with dynamic values 
#---see carefully the formating of multi-line sql statement

import cx_Oracle

con = cx_Oracle.connect('system', 'admin123', 'localhost:1521/XE')

cursor = con.cursor()

name = 'Neethu'
lname = 'Sani'

sql = "INSERT INTO Professional(FIRST_NAME,\
   LAST_NAME, AGE, GENDER, INCOME) \
   VALUES('%s', '%s', '%d', '%s', '%f') " %\
   (name,lname,28,'F',30000)

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   con.commit()
except:
   # Rollback in case there is any error
   con.rollback()

con.close()   

#-------------------------------------------

#--Coding Exercise : 5
#---Update a record
import cx_Oracle
from pprint import pprint

con = cx_Oracle.connect('system', 'admin123', 'localhost:1521/XE')

cursor = con.cursor()
sql= "Update professional1 set AGE= AGE+1 where firstname='zoya'"

try:
    cursor.execute(sql)
    con.commit()
except:
    con.rollback()
con.close()





#--------------------------------------------

#--Coding Exercise : 6
#--deleting a record  
import cx_Oracle

con = cx_Oracle.connect('system', 'admin123', 'localhost:1521/XE')

#--your code here 





#---------------------------------

##---------Project Assignment----------

#--Research and code :
#--Fetch data values from user and insert records into your table. Assume employees table with 4-5 columns exist. Ask the user whether he wants to enter record, if Yes -> 1 , if No -> 0. If user says 1 then accept the column values and insert into the table. The loop should continue till user enters 0
#-------------------------------


import cx_Oracle

con = cx_Oracle.connect('system', 'admin123', 'localhost:1521/XE')
cursor = con.cursor()
while True:

    choice=input("Do you want input record If yes press 1 else press 0")
    if choice=="0":
        print("Exiting Program...")
        break
    elif choice=="1":
        ei=int(input("EMPID"))
        en=str(input("EMPNAME"))
        sal=float(input("SALARY"))
        dept=str(input("DEPT"))
        desig=str(input("DESIGNATION"))
        print (ei, en, sal,dept ,desig)
        sql = "INSERT INTO empdadar(EMPID,\
   EMPNAME, SALARY, DEPT, DESIGNATION) \
   VALUES('%d', '%s', '%f', '%s', '%s') " %\
   (ei,en,sal,dept,desig)
    
        cursor.execute(sql)

        con.commit()

con.close()


