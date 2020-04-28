#--multi-threading in python 

#--creating 2 threads, finding active threads : activeCount()  
import threading

class myThread (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      
   def run(self):
      print("Starting " + self.name)
      print("Id of the Thread : " + str(self.threadID))
	  

# Create new threads
thread1 = myThread(1, "Thread-1")
thread2 = myThread(2, "Thread-2")

# Start new Threads
thread1.start()
thread2.start()
print(threading.activeCount()) #get no. of threads
thread1.join()
thread2.join()
print("Exiting Main Thread")
#----------------------------------------

#--creating threads and printing its details
import threading

class myThread (threading.Thread):
   def __init__(self):
      threading.Thread.__init__(self)
      
      
   def run(self):
      print(threading.currentThread())
	  

# Create new threads
thread1 = myThread()
thread2 = myThread()

# Start new Threads
thread1.start()
thread2.start()
print(threading.currentThread())
thread1.join()
thread2.join()
print("Exiting Main Thread")

#----------------------------------------
#--Running 2 threads with a delay
#--for delay use module time
#--time.sleep(delay_in_secs)

import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   
   def run(self):
      print ("Starting " + self.name)
      print_time(self.name, self.counter, 5)
      print ("Exiting " + self.name)

def print_time(threadName, delay, counter):
    while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("Exiting Main Thread")


#-----------------------------------------------

#--Synchronizing Threads using threading.Lock()
#-- on Lock Object -> acquire() and release()  

import threading
import time

class myThread(threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
	  
   def run(self):
      print ("Starting " + self.name)
      # Get lock to synchronize threads
      threadLock.acquire()
      print_time(self.name, self.counter, 3)
      # Free lock to release next thread
      threadLock.release()

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")

#------------------------------------

#--Multi-threaded Priority Queue
#--understanding synchronized consumption of data

import queue
import threading
import time

exitFlag = 0

class myThread(threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
   def run(self):
      print ("Starting " + self.name)
      process_data(self.name, self.q)
      print ("Exiting " + self.name)

def process_data(threadName, q):
   while not exitFlag:
      queueLock.acquire()
      if not workQueue.empty():
         data = q.get()
         queueLock.release()
         print ("%s processing %s" % (threadName, data))
      else:
         queueLock.release()
         time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
   thread = myThread(threadID, tName, workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
   workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
   pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")

#-------------------------------------------

#--another way of Thread programming :
#--without creating a sub-class
#--without explicitly coding run()

import threading 
  
def print_cube(num): 
    """ 
    function to print cube of given num 
    """
    print("Cube: {}".format(num * num * num)) 
  
def print_square(num): 
    """ 
    function to print square of given num 
    """
    print("Square: {}".format(num * num)) 
  
if __name__ == "__main__": 
    # creating thread 
    t1 = threading.Thread(target=print_square, args=(10,)) 
    t2 = threading.Thread(target=print_cube, args=(10,)) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
  
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
  
    # both threads completely executed 
    print("Done!") 


#--------------------------------------------------------

#--Coding exercise : 1 : 
#--Threads belong to a process. 
#--we can get the Id of the Process, to which the threads belong.
import threading 
import os 
  
def task1(): 
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name)) 
    print("ID of process running task 1: {}".format(os.getpid())) 
def task2():
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name)) 
    print("ID of process running task 2: {}".format(os.getpid()))

  
if __name__ == "__main__": 
    # print ID of current process 
    print("ID of process running main program: {}".format(os.getpid())) 
  
    # print name of main thread 
    print("Main thread name: {}".format(threading.main_thread().name)) 
  
    # creating threads 
    #----your code here----  
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')
    # starting threads 
    #----your code here----  
    t1.start()
    t2.start()
    
    # wait until all threads finish 
    #----your code here----   
    t1.join()
    t2.join()
#---------------------------------------
#-- find outputs :
#--Q1>  --In notes--
#-----
#Ans 1>  threads array is not used in above prg.
#-----
	
#--Q2> --In notes--
#-----
#Ans 2>  threads array is used to hold all thread objects.
#-----

#--Q3> --In notes--
#-----
#Ans 3>  depends on scheduling. Here the o/p looks exactly in the same sequence as you have started (i.e. called start()), because the thread body is too short and gets completed in the minimum time slice given to it. Thread Scheduler uses Round Robin Algo.
#-----


#--Q4> --In notes--
#-----
#- Q4> Which class is MyThread extending from ?
#--A4> It is extending from threading.Thread
#----- 

#--Q5>
#--Run this program. Write your observations
#-- A Timer starts its work after a delay, and can be canceled at any point within that delay time period.

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def delayed():
    logging.debug('worker running')
    return

t1 = threading.Timer(3, delayed)
t1.setName('t1')
t2 = threading.Timer(3, delayed)
t2.setName('t2')

logging.debug('starting timers')
t1.start()
t2.start()

logging.debug('waiting before canceling %s', t2.getName())
time.sleep(2)
logging.debug('canceling %s', t2.getName())
t2.cancel()
logging.debug('done')

#---Points w.r.t Q5 : program :
1> Instead of printing we are logging. Its a better practice.
2> to log use  logging.debug(string str) 
3> We have to specify level in 
logging.basicConfig()	
4> format is optional. Try running the code with / without format parameter.
#---------------------------------------------

#--Q6>
#--Run this program. Write your observations.
#--Its a simple solution to producer consumer problem

import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-2s) %(message)s',
                    )

def consumer(cond):
    """wait for the condition and use the resource"""
    logging.debug('Starting consumer thread')
    t = threading.currentThread()
    with cond:
        cond.wait()
        logging.debug('Resource is available to consumer')

def producer(cond):
    """set up the resource to be used by the consumer"""
    logging.debug('Starting producer thread')
    with cond:
        logging.debug('Making resource available')
        cond.notifyAll()

condition = threading.Condition()
c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
p = threading.Thread(name='p', target=producer, args=(condition,))

c1.start()
time.sleep(2)
c2.start()
time.sleep(2)
p.start() 

#---------------------------------  	
#--w.r.t Q6 answer the following questions
#--Q6.1> Explain the purpose of making Condition object ? 
#--condition = threading.Condition()
Ans 6.1 > Its like a Event Object on which two or more threads can synchronise.


#--Q6.2> What's the role of wait() call ? 
#--cond.wait()
Ans 6.2> Its a blocking call, indicating to wait till the completion of an event. Here the event is the producer producing some data. 



#--Q6.3> What's the difference between notify() and nofityall() ? 
Ans 6.3> Both methods indicate the the event some other thread is waiting for is done. notify() would inform only the first waiting thread in the Queue. while nofityall() would inform all threads in the Queue. Now after nofityall() its the decision of the Python Thread scheduler on which threads it picks up for running. Hence after nofityall(), we cant say which out of the many waiting threads would start running first.
