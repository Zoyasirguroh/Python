#-- regex and many regex based application --
#---------------------------------
A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern. 

The module re provides full support for Perl-like regular expressions in Python. The re module raises 
the exception re.error if an error occurs while compiling or using a regular expression.
#----------------------------------

#--Regular Expressions called Regex
#--Understand power of Regex
#--Finding Patterns of Text Without Regex
#--is a hard work, not smart work
def isPhoneNumber(text):
 
 if len(text) != 13:
  return False
 
 for i in range(0, 3):
  if not text[i].isdecimal():
   return False
 
 if text[3] != '-':
  return False
 
 for i in range(4,8):
  if not text[i].isdecimal():
   return False

 if text[8] != '-':
  return False
 
 for i in range(9,13):
  if not text[i].isdecimal():
   return False
  
 return True
  
print('022-2527-7413 is a phone number:', end='')
print(isPhoneNumber('022-2527-7413'))
print('SCTPL is a phone number:', end='')
print(isPhoneNumber('SCTPL'))
#--------------------------------
#--------------------------------

#--Finding Patterns of Text with Regular Expressions
#-----------------------------------------
The regex \d\d\d-\d\d\d\d-\d\d\d\d is used
by Python to match the same text in the previous isPhoneNumber()
#-----------------------------------------

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 022-2527-7413.')

#return value of search is match_object or NONE 
if mo :
 print('Phone number found: ' + mo.group())<---- #if u use str() instead of  group() it will return the start n  end of phone number

#-----------------------------------------
#--form groups by using ()
#--printing state code and the no. 
import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 022-2527-7413.')

if mo :
 print('State code is : ' + mo.group(1))
 print('And the number is : ' + mo.group(2))
 print('and the entire no. is : ', mo.group())

#----------------

#--rewriting the above code and printing all groups
import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 022-2527-7413.')

if mo :
 print(mo.groups())

#--------------
#--Matching Multiple Groups with the Pipe |
#--------------
import re

heroRegex = re.compile(r'Airlift|Akshay kumar')
mo1 = heroRegex.search('Akshay kumar in Airlift.')
if mo1 :
 print(mo1.group())

mo2 = heroRegex.search('Airlift starred Akshay kumar.')
if mo2 :
 print(mo2.group())

#------------------

#--use pipe to match one of several patterns
import re

batRegex = re.compile(r'Bat(man|mobile|ball|Cricket)')
mo = batRegex.search('Batmobile lost a wheel')
if mo :
 print(mo.group())
 print(mo.group(1))

#--another example
mo = batRegex.search('Batball is galli cricket')
if mo :
 print(mo.group())
 print(mo.group(1))

#-------------
#--Optional Matching with the Question Mark
import re

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
if mo1 :
 print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
if mo2 :
 print(mo2.group())
 
#--------------
#-- another ex. : state-code 022 is optional
import re

phoneRegex = re.compile(r'(\d\d-)?\d\d\d\d\d-\d\d\d\d\d')
mo1 = phoneRegex.search('My number is 91-98700-14450')
if mo1 :
 print(mo1.group())

mo2 = phoneRegex.search('My number is 98700-14450')
if mo2 :
 print(mo2.group())

#----------------

#--Matching Zero or More with the Star

import re

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
if mo1 :
 print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
if mo2 :
 print(mo2.group())
 
mo3 = batRegex.search('The Adventures of Batwowowowoman')
if mo3 :
 print(mo3.group())

#------------------

#--Matching One or More with the Plus
import re 

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
if mo1 :
 print(mo1.group())
else :
 print("input string does not contain pattern")


mo2 = batRegex.search('The Adventures of Batman')
if mo2 :
 print(mo2.group())
else :
 print("input string does not contain pattern")

#------------

#--Matching Specific Repetitions with Curly Brackets
import re

#-- can match one, two, or three instances of fine 
chatRegex = re.compile(r'(fine){1,3}')
mo1 = chatRegex.search('I am fine thank you. fine so your team would be their ? ')

if mo1 :
 print(mo1.group())
 
#---------------
#--Greedy and Non-greedy Matching
#--{1,3} -> is Greedy matching
#--{1,3}? -> is non-Greedy matching

import re

greedyHaRegex = re.compile(r'(Ha){1,3}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
if mo1 :
 print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){1,3}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
if mo2 :
 print(mo2.group())
 
#---findall() Method
#-- search() will return a Match object of the first matched text in the searched string, the findall() method will return the strings of every match in the searched string.
#--------- ex : findall() 
 
import re

phoneNumRegex = re.compile(r'\d\d\d\d\d-\d\d\d\d\d')
mo1 = phoneNumRegex.search('Cell: 98925-44177 Work: 98700-14450')
if mo1 :
 print(mo1.group())


phoneNumRegex = re.compile(r'\d\d\d\d\d-\d\d\d\d\d')
mo2 = phoneNumRegex.findall('Cell: 98925-44177 Work: 98700-14450')

#return type of findall() is a list. 
if mo2 :
 print(mo2)

#--------------
#--ex:2 on findall() on regex with groups
import re

#as regex has groups*
phoneNumRegex = re.compile(r'(\d\d\d\d\d)-(\d\d\d\d\d)')
mo = phoneNumRegex.findall('Cell: 98925-44177 Work: 98700-14450')

#*hence return type of findall() is a list of tuples. 
if mo :
 print(mo)

#------------------------
#--Character Classes : \d, \D, \w, \W, \s, \S
#------------------------
#--using Character Classes----
import re

coursesRegex = re.compile(r'\d+\s\w+')
mo = coursesRegex.findall('1 Java-1z0-808, 2 SQL Oracle-1z0-061, 33 Web-Technologies, 34 Textile Designing')

if mo :
 print(mo)
 
#-------------------------

#--Making Your Own Character Classes
#---------------
#---Coding Exercise : 1
#- example : find all vowels in a sentence
import re

#your code here 
 
 vowelregex = re.compile(r'[aeiouAEIOU]')
mo = vowelregex.findall('RoboCop eats baby food BABY FOOD.')

if mo:
    print(mo)
 
#---------------------
#---Coding Exercise : 2
#-- find all letters other than vowels
# using ^ makes a negative character class
import re

#---your code here 
vowelregex = re.compile(r'[^aeiouAEIOU]')
mo = vowelregex.findall('RoboCop eats baby food BABY FOOD.')

if mo:
    print(mo)

#-----------

#--Coding Exercise : 3 : Type and run this code : 
#--see the difference of using ^ without [] 
# using (^Hello) means string starts with Hello
import re

beginsWithHello = re.compile(r'^Hello')

#---your code here---
mo1=beginsWithHello.search('hello world!')
if mo1:
    print(mo1.group())

mo2=beginsWithHello.search('he said hello')
if mo2== None:
    print(mo2)

 
#------------------
#--Coding Exercise : 4 
#--using $ means ends with
import re

#---your code here---
endswithnumber = re.compile(r'\d$')

mo1= endswithnumber.search('number is 42.')
if mo1:
    print(mo1)

mo2= endswithnumber.search('number is forty two.')
if mo2== None:
    print(mo2)

#------------------

#--Coding Exercise : 5 
# using ^(starts with), +(1 or more), $(ends with)
import re

wholeStringIsNum = re.compile(r'^\d+$')

#---your code here---

mo1= wholeStringIsNum.search('123456789')
if mo1:
    print(mo1)

mo2= wholeStringIsNum.search('12345xyz7890')
if mo2== None:
    print(mo2)
    
mo3= wholeStringIsNum.search('12 3456789')
if mo3== None:
    print(mo3)



#--------------------- 
#--Coding Ex : 6 : Type and run this code 
#- .(dot) the Wildcard Character
# .(dot) will match any character except newline.
import re

atRegex = re.compile(r'.at')

#---your code here---
mo1=atRegex.findall('the cat in the hat sat on the flat mat.')
if mo1:
    print(mo1)



#--------------------- 
#--Coding Ex : 7
#--Matching Everything with Dot-Star
# .(dot) will match any character except newline.


#---your code here---
import re

nameRegex = re.compile(r'First Name:(.*) Last Name:(.*)')

mo1=nameRegex.search('First Name: Zuhrah Last Name: Sirguroh')
if mo1:
    print(mo1.group(1))
    print(mo1.group(2))


#------------
#--Coding ex: 8 
#  To match any and all text in a nongreedy fashion, use the dot, star, and question mark (.*?) 

#---your code here---
import re

nongreedyRegex = re.compile(r'<.*?>')

mo1=nongreedyRegex.search('<To serve paneer> for dinner.>')
if mo1:
    print(mo1.group())
    
greedyRegex = re.compile(r'<.*>')

mo2=greedyRegex.search('<To serve paneer> for dinner.>')
if mo2:
    print(mo2.group())

 
 
#------------
#--coding ex: 9
#--Matching Newlines with the Dot Character
#-----------------------
Note: The dot-star will match everything except a newline. By passing re.DOTALL as the second argument to re.compile(), you can make the dot character match all characters, including the newline character.
#--------------------------
import re

noNewlineRegex = re.compile('.*')
mo1 = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')

if mo1 :
 print("no new line :", mo1.group())

print("------------------------------")

newlineRegex = re.compile('.*', re.DOTALL)
mo2 = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')

if mo2 :
 print(mo2.group())

#-------------------------
#--Case-Insensitive Matching--
#--Normally, regular expressions match text with the exact casing you specify. To make your regex case-insensitive, you can pass re.IGNORECASE or re.I as a second argument to re.compile().
#-------------------------
#--ex: 10
import re

robocop = re.compile(r'robocop', re.I)

#cascaded all statements 
print(robocop.search('RoboCop is part man, part machine, all cop.').group())

#-------------------------
#--Substituting Strings with the sub() Method
#-------------------------

#--ex: 11
import re

#-- \w -> any char except space
namesRegex = re.compile(r'Agent \w+')

mo = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')

if mo :
 print(mo)

#---------------------
#--ex: 12 : little complex example
#------------
Note :  say you want to censor the names of the secret agents by showing just the first letters of their names. To do this, you could use the regex Agent (\w)\w* and pass r'\1****' as the first argument to sub(). 
The \1 in that string will be replaced by whatever text was matched by group 1— that is, the (\w) group of the regular expression.
#------------
#--- Hide the names of agents ---
import re

agentNamesRegex = re.compile(r'Agent (\w)\w*')

mo = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')

if mo :
 print(mo)
 
import re

agentNamesRegex = re.compile(r'Agent (\w)(\w)\w*')

mo = agentNamesRegex.sub(r'\2****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')

if mo :
 print(mo)

#---------------
#--Managing Complex Regexes
#--ex: 13 : Regex to check a phone number
#---------------
import re

phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{4}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

mo1 = phoneRegex.search('Your no. is 022-2527-7413 ext 123')

if mo1 :
 print(mo1)
else :
 print("none")

mo2 = phoneRegex.search('Your no. is (022)-2527-7413')

if mo2 :
 print(mo2.group())
else :
 print("none") 
 
mo3 = phoneRegex.search('Your no. is 98700-14450')

if mo3 :
 print(mo3.group())
else :
 print("none")  

#--------------
#--ex:14: Regex to check phone number, using VERBOSE
#--you can spread the regular expression over multiple lines with comments like this:
#--------------
import re

phoneRegex = re.compile(r'''(
 (\d{3}|\(\d{3}\))?             #area code
 (\s|-|\.)?                     #separator
 \d{4}                          #first 4 digits
 (\s|-|\.)                      #separator
 \d{4}                          #last 4 digits
 (\s*(ext|x|ext.)\s*\d{2,5})?   # extension
 )''', re.VERBOSE)

mo1 = phoneRegex.search('Your no. is 022-2527-7413 ext 123')

if mo1 :
 print(mo1)
else :
 print("none")

mo2 = phoneRegex.search('Your no. is (022)-2527-7413')

if mo2 :
 print(mo2.group())
else :
 print("none") 
 
mo3 = phoneRegex.search('Your no. is 98700-14450')

if mo3 :
 print(mo3.group())
else :
 print("none")  
#----------------
Explaination to the phoneRegex :

The phone number begins with an optional area code, so the area code group is followed with a question mark. Since the area code can be just three digits (that is, \d{3}) or three digits within parentheses (that is, \(\d{3}\)), you should have a pipe joining those parts. 

The phone number separator character can be a space (\s), hyphen (-), or period (.), so these parts should also be joined by pipes. 

The last part is an optional extension made up of any number of spaces followed by ext, x, or ext., followed by two to five digits. 
#------------------- 
