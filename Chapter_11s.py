#-----Working with CSV and Json data
CSV stands for "comma-separated values" and CSV files are simplified spreadsheets stored as plaintext files. Python's csv module makes it easy to parse CSV files.

Each line in a CSV file represents a row in the spreadsheet, and commas separate the cells in the row.
#---------------------------------------------------

#--reading from a .csv file
import csv
exampleFile = open('suven/example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(exampleData)

#-----------------------------

#--To access any particular cell entry using indexing
import csv
exampleFile = open('suven/example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print("printing the first cell entry")
print("------------------------------")
print(exampleData[0][0], '\n')
print(exampleData[0][1], '\n')
print(exampleData[0][2], '\n')

#----------------------------------------

#--Reading Data from Reader Objects in a for Loop
import csv
exampleFile = open('suven/example.csv')
exampleReader = csv.reader(exampleFile)

for row in exampleReader:
 print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
 
#---------------------------------------

#--Writer Object : lets write to a csv file
import csv
outputFile = open('suven/output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

outputWriter.writerow(['Suven','Consultants','Python','IBM'])
outputWriter.writerow(['Hello, world!','eggs','bread','tea'])
outputWriter.writerow([1, 2, 3.141592, 4])
outputFile.close()

#--Note : if you forget to set the newline argument, the rows in output.csv will be double-spaced. Try it.
#----------------------------------------

#--Project :
You have the boring job of removing the first line from several hundred CSV files. Maybe you’ll be feeding them into an automated process that requires just the data and not the headers at the top of the columns. You could open each file in Excel, delete the first row, and resave the file—but that would take hours. Write a program to do it instead.

Expected from the Program :
The program will need to open every file with the .csv extension in the current working directory, read in the contents of the CSV file, and rewrite the contents without the first row to a file of the same name. This will replace the old contents of the CSV file with the new, headless contents.
#-----------------------------------------------------

At a high level, the program must do the following:
• Find all the CSV files in the current working directory.
• Read in the full contents of each file.
• Write out the contents, skipping the first line, to a new CSV file. 

#------------------------------------------------------

Coding Steps :
At the code level, this means the program will need to do the following: 
• Loop over a list of files from os.listdir(), skipping the non-CSV files.
• Create a CSV Reader object and read in the contents of the file, using the line_num attribute to figure out which line to skip.
• Create a CSV Writer object and write out the read-in data to the new file.
#-----------------------------------------

#your project code here

import csv, os

os.makedirs('suven/headerremoved', exist_ok=True)

for csvFilename in os.listdir('./suven'):
    if not csvFilename.endswith('.csv'):
        continue 
    else:
        print('Removing header from'+csvFilename+'...')
        csvRows=[]
        csvFilenameR="suven/"+str(csvFilename)
        
        csvFileObj=open(csvFilenameR)
        readerObj=csv.reader(csvFileObj)
        
        for row in readerObj:
            if readerObj.line_num==1:
                continue 
            csvRows.append(row)
        csvFileObj.close()
    
    csvFileObj = open(os.path.join('suven/headerremoved',csvFilename), 'w', newline='')
    csvWriter=csv.writer(csvFileObj)
    
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()



#-----------------------------------------
JSON is a format that stores information as JavaScript source code in plaintext files. (JSON is short for JavaScript Object Notation) The JSON format is useful to know because it’s used in many web applications.
#-----------------------------------------

#--Reading JSON with the loads() Function
stringOfJsonData = '{"name": "Catty", "isCat": true, "miceCaught": 0, "felineIQ": null}'

import json
jsonDataAsPythonValue = json.loads(stringOfJsonData)

print(jsonDataAsPythonValue)

#------------------------------------------
#--Writing JSON with the dumps() Function
#--dumps means dump string
#--The process of encoding JSON is called serialization.
#--De-serialization is the reciprocal process of decoding data that has been stored or delivered in the JSON standard.
#------------------------------------------

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Catty',
'felineIQ': None}

import json
stringOfJsonData = json.dumps(pythonValue)

print(stringOfJsonData)

#------------------------------------------
#--reading json data and writing to a file
import json

data = {
    "president": {
        "name": "Ram Nath Kovind",
        "native": "Uttar Pradesh"
    }
}

with open("suven/data_file.json", "w") as write_file:
    json.dump(data, write_file)

#----------------------------------------

#--reading json data from a file and printing it.
import json

with open("suven/data_file.json", "r") as read_file:
    str = read_file.read(1000)
    print(json.loads(str))
	
	
#----------------------------------------

#--formatting data in dumps()
import json

data = {
    "president": {
        "name": "Ram Nath Kovind",
        "native": "Uttar Pradesh"
    }
}

print(json.dumps(data))

print("--------------------------------")

#after formatting data
print(json.dumps(data, indent=4))


#----------------------------------------
#--Project idea: Fetching Current Weather Data
#----------------------------------------
Algorithmic Steps :
Reads the requested location from the command line.
• Downloads JSON weather data from OpenWeatherMap.org.
• Converts the string of JSON data to a Python data structure.
• Prints the weather for today and the next two days.
#----------------------------------------------------------

Coding Steps:
• Join strings in sys.argv to get the location.
• Call requests.get() to download the weather data.
• Call json.loads() to convert the JSON data to a Python data structure.
• Print the weather forecast.
#----------------------------------------------------------

