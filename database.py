import cx_Oracle

con = cx_Oracle.connect('system', 'admin123', 'localhost:1521/XE')

choice=input("Do you want input record If yes press 1 else press 0")
while True:

    if choice ==0:
        exit()
    else:
        ei=int(input("EMPID"))
        en=str(input("EMPNAME"))
        sal=float(input("SALARY"))
        dept=str(input("DEPT"))
        desig=str(input("DESIGNATION"))
        print (ei, en, sal,dept ,desig)
        sql = "INSERT INTO empdadar(FIRST_NAME,\
   LAST_NAME, AGE, GENDER, INCOME) \
   VALUES('%d', '%s', '%f', '%s', '%s') " %\
   (ei,en,sal,dept,desig)
    