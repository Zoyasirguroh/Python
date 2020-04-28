#-- web scraping 
#-- Modules needed and built-in in python ----
webbrowser : Comes with Python and opens a browser to a specific page.
Requests : Downloads files and web pages from the Internet.
Beautiful Soup : Parses HTML, the format that web pages are written in.
Selenium : Launches and controls a web browser. Selenium is able to fill in forms and simulate mouse clicks in this browser.
#---------------------------------------------

#--open a web page from your script
import webbrowser
webbrowser.open('https://suvenconsultants.com//')

#-----bring up a Google map for the address-----
#--steps :
1> Gets a street address from the command line arguments
2> Open the web browser to the Google Maps page for the address.
#----------------
#-- e.g : if you want enter "Suven Consultants chembur"
#-- then the link to show maps looks like this : 
https://www.google.com/maps/place/Suven+
Consultants+chembur/
#-----------------------------------
#-- coding Ex
import webbrowser, sys

if len(sys.argv) > 1:
 # Get address from command line.
    address=' '.join(sys.argv[1:])
    webbrowser.open('https://www.google.com/maps/place/'+address)
 #--- your code here ---
 
 
 
#try running the code with some address
#like suven consultants chembur mumbai 

#--------------------------------

#-Downloading Files from the Web with the requests Module

#-- download requests module ---
pip install requests
#-------------------

#--Downloading a Web Page with requests.get() function
import requests

res = requests.get('https://training.suven.net/')

#check the response object
print(type(res))

if res.status_code == requests.codes.ok :
 len(res.text)
 print(res.text[:251])

#----------------
#-- to know about other request codes :
import requests

print(requests.codes.processing)  # returns 102
print(requests.codes.ok)          # returns 200
print(requests.codes.not_found)   # returns 404
#----------------

#--Checking for Errors--
#-------------
Note : The raise_for_status() method is a good way to ensure that a program halts if a bad download occurs. This is a good thing: You want your program to stop as soon as some unexpected error happens.
#-------------

import requests
res = requests.get('http://suven.net/no_page.html')

try:
 res.raise_for_status()
except Exception as exc:
 print('There was a problem: %s' % (exc))

#--------------
Note : Always call raise_for_status() after calling requests.get(). You want to be sure that the download has actually worked before your program continues.
#--------------

#--Saving Downloaded Files to the Hard Drive

import requests
res = requests.get('https://feedback.suven.net/')
try:
 res.raise_for_status()
 trainingFile = open('suven/feedbackHtmlCode.html', 'wb')
 
 for chunk in res.iter_content(1000):
  trainingFile.write(chunk)
  
 trainingFile.close()

except Exception as exc:
 print('There was a problem: %s' % (exc))

#----------------

#--Parsing HTML with the BeautifulSoup Module--

#---- install BeautifulSoup Module
pip install beautifulsoup4
#--------------------------------- 

#---scraping a web page and finding all <a> tags
import requests, bs4

res = requests.get('https://suven.net')
res.raise_for_status()
textDataForParsing = bs4.BeautifulSoup(res.text, features='lxml')  # lxml is specification for the parser

elements = textDataForParsing.select('a')
print(type(elements))

print("# of <a> tags are :",len(elements))

for i in range(0,5) :
 print(type(elements[i]))
 print("--------------------")
 print(elements[i].getText())
 print("--------------------")
 print(str(elements[0]))
 print("--------------------")
 print(elements[0].attrs)
 print("--------------------")
 
#------------------------------------

#-- Project : Automate Google Search :
#--------------------------------------
Problem Definition : Whenever I search a topic on Google, I don’t look at just one search result at a time. By middle-clicking a search result link, I open the first several links in a bunch of new tabs to read later.
I search Google often enough that this workflow—opening my browser, searching for a topic, and middle-clicking several links one by one—is tedious. It would be nice if I could simply type a search term on the command
line and have my computer automatically open a browser with all the top search results in new tabs.
 
Write a script to do this.
#-------------------------------------------------
Algorithm :
1> Gets search keywords from the command line arguments.
2> Retrieves the search results page.
3> Opens a browser tab for each result.

Implementation steps 
This means your code will need to do the following:
a> Read the command line arguments from sys.argv.
b> Fetch the search result page with the requests module.
c> Find the links to each search result.
d> Call the webbrowser.open() function to open the web browser.

#--------------------------

#-- version 1: ----------

import requests, sys, webbrowser, bs4

# display text while downloading the Google page
print('Googling...') 

res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#TODO: Retrieve top search result links.

#TODO: Open a browser tab for each result.

#---------------------------

#--- final version ---


#---your code here


import requests, sys, webbrowser, bs4

# display text while downloading the Google page
print('Googling...') 

res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result. 
# Assuming all <a> links are results. Although this assumption is wrong.
linkElems = soup.select("a")

print(len(linkElems))

numOpen = min(25,len(linkElems)) # min of 25 tabs.

# we are opening from 15th to numOpen no. of tabs. 
# Because first 10 to 15 <a> tags are links to Google home page, youtube, etc...
# Mostly our first search result starts from the 15th or above <a> link. 
for i in range(15, numOpen):
 webbrowser.open('http://google.com' + linkElems[i].get('href'))





#----------------------------------------------
#-- Additional Reading -- for testers --
#----------------------------------------------
#--using selenium Module
#---------------------
pip install selenium
#---------------------
#--Controlling the Browser with the selenium Module
#-----------------
Note : The selenium module lets Python directly control the browser by programmatically clicking links and filling in login information, almost as though there is a human user interacting with the page.
#-----------------------------------------
Refer below link for resources :
https://pythonspot.com/selenium-webdriver/
#-----------------------------------------
