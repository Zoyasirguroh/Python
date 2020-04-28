#--Scheduling task and launching programs
#--------------------------------------------
#--The Unix epoch is a time reference commonly used in programming: 12 am on January 1, 1970,. The time.time() function returns the number of seconds since that moment as a float value.
#---------------------------------------------
import time
print(time.time())
#---------------------------------------------

#--find time taken to execute a piece of code.
import time

def calcProd():
 product = 1

 for i in range(1, 100000):
  product = product * i
 
 return product

startTime = time.time()
prod = calcProd()
endTime = time.time()

print('The result is %s digits long.' %(len(str(prod))))
print('Took %s seconds to calculate.' %(endTime - startTime))

#----------------------------------------------

#--use of sleep(n secs) 
#--try CTRL-C and you would see KeyboardInterrupt Exception
import time

for i in range(3):
  print('Tick')
  time.sleep(1)
  print('Tock')
  time.sleep(1)


#-----------------------------------------------

#--The datetime Module--------------------------
The datetime module has its own datetime data type. datetime values represent a specific moment in time.
#-----------------------------------------------

import datetime

#--present datetime 
print(datetime.datetime.now())

#--making a datetime object
dt = datetime.datetime(2018, 12, 21, 16, 29, 0)

print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second)

#-----------------------------------------------

#--A Unix epoch timestamp can be converted to a datetime object with the datetime.datetime.fromtimestamp() function

import datetime, time

print(datetime.datetime.fromtimestamp(1000000))

print(datetime.datetime.fromtimestamp(time.time()))

#-----------------------

#--Pausing Until a Specific Date and time
import datetime
import time

traditionalDay = datetime.datetime(2019, 2, 22, 14, 57, 0)

while datetime.datetime.now() < traditionalDay:
 time.sleep(1)


#----------------------------------------------
#--Launching Other Programs from Python
Your Python program can start other programs on your computer with the Popen() function in the built-in subprocess module.
#----------------------------------------------

#-- opening calculator application
  
import subprocess
subprocess.Popen('C:\\Windows\\System32\\calc.exe')

#-----------------------------------------------

#--return value is a Popen object, has two useful methods: poll() and wait().

#--Note that the wait() call will block until you quit the launched calculator program.

import subprocess

calcProc = subprocess.Popen('c:\\Windows\\System32\\calc.exe')

#--The poll() method will return None if the process is still running
if calcProc.poll() == None :
 calcProc.wait() #wait is blocking call
else :
 print(calcProc.poll())
 
#---------------------------------------

#--open a process or application and with in a file.
import subprocess
subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\test.txt']) 

#---------------------------------------

#--Mini-Project 1: Super Stopwatch
Your super-stopwatch should 
1> Track the amount of time elapsed between presses of the enter key. 
2> With each key press starting a new "lap" on the timer.
3> Print the lap number, total time, and lap time.
#--------------------------------

Coding steps for super-stopwatch :
This means your code will need to do the following:
• Find the current time by calling time.time() and store it as a timestamp at the start of the program, as well as at the start of each lap.
• Keep a lap counter and increment it every time the user presses enter.
• Calculate the elapsed time by subtracting timestamps.
• Handle the KeyboardInterrupt exception so the user can press ctrl-C to quit.
#-------------------------
import time

print('print enter to begin. afterwards, press enter to click the stopwatch . press ctrl+c to quit')

input()

print('started.')
startTime= time.time()
lastTime= startTime
lapNum=1

try:
    while True:
        input()
        lapTime=round(time.time()-lastTime,2)
        totalTime=round(time.time()-startTime,2)
        print('Lap #%s:%s (%s)'%(lapNum,totalTime,lapTime),end=' ')
        lapNum+=1
        lastTime=time.time()
except KeyboardInterrupt:
    print('\n done')




#-------------------------


#--Mini-Project 2: Simple Countdown Program

#--your project code here
import time , subprocess

timeLeft = 5

while timeLeft > 0 :
    print(timeLeft)
    time.sleep(1)
    timeLeft = timeLeft-1

subprocess.Popen(['start','‪‪C:\\Users\\Zuhrah\\Desktop\\2019-10-12 17-53-20.mp4'],shell=True)
#----------------------------