# Module 7: Pickling and Error Handling in Python

## Introduction
Learning objective of module 07 is to learn about Exception handling and Pickling module in Python and to get familiar with advanced publishing in GitHub. We were encouraged to seek our own external sources of information related to Pickling and Exception handling. 
## Pickling
Sometimes it is important to reduce file’s size or to obscure its contents. In these cases, output could be saved in a binary format. Pickling is a Python serialization method for converting objects and their hierarchy using binary protocols. Python pickle module is used to store data in binary files and ‘unpickling’ (reading) data back from these files. According to documentation on python.org [External file], pickling method is not secure and should only be used for trusted data. Pickled data can be malicious and may execute harmful code during unpickling. Additionally, pickling data makes it obscure (hard to read for a human eye) but not secure, since it is not encrypted. To use pickle module in Python script, type: 
 import pickle 
## What type of data can be pickled?
Boolean, integer, floating point numbers, strings, tuples, lists, dictionaries and even functions and classes!
Access mode for binary files
rb Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.
wb Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
ab Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing. 
Source: https://www.tutorialspoint.com/python/python_files_io.htm [External file]
Example:
objFile=open("AppData.dat","rb")
This opens file AppData.dat for reading in binary format.




## Pickling functions dump and load
To write pickled data to a binary file use dump function:
pickle.dump(obj, file)

This writes pickled data (obj parameter) to opened file (file parameter). 

To read pickled data from a binary file, use load function:

pickle.load(file)

## Protocols
Converting (pickling) data is executed according to one of the available protocols. Currently there are 5 protocols (versions). Protocol is an optional parameter for dump and load functions. If not specified, default protocol for Python interpreter will be used. Usually default = the highest protocol, but not always.
## Error Handling
Python handles most programming errors automatically via built-in class called ‘Exception’. It is used to hold information about several types of common errors. These errors could be captured and extracted by assigning them to a variable. To do that, try-except method is used, as shown in Figure 1.

try:
    quotient = 5/0
    print(quotient)
except Exception as e:
    print("Error!”)   #any custom message could go in here
    print (e)

 Figure 1. Example of try-except method

Specific error types
Exception is a class that captures all types of error, but sometimes we need to be more specific. There are error types that can help with that. Here are some examples:
ValueError
FileNotFoundError
ZeroDivisionError


Figure 2 shows example of using specific error type ZeroDivisionError:

try:
    quotient = 5/0
    print(quotient)
except ZeroDivisionError as e:
    print("Error! You can’t divide by 0!”)   #any custom message could go in here
except Exception as e:                      #any other errors will still be captured by general Exception
    print("Error!”)   
    print (e)

 Figure 2. Example of try-except method with specific error type

## Raising Custom Exception
In addition to specific error types custom errors can be defined (raised). For example, if you want to user input to be only positive numbers, you can use the custom exception as shown in Figure 3:

while True:
    try:
intNumber = int(input("People vaccinated: "))
if intNumber < 0:  # raising custom exception
    raise Exception("Number must be >= 0")
else:
    return lstData
    except Exception as e:  # this exception catches all the rest
    print("There was a non-specific error!")
    print(e)

Figure 3. Raising custom expression

# Assignment 07
Objective: Write script that shows examples of using pickling and error handling. 
Program description: My program will collect vaccination statistics for various cities. It then will pickle information into binary file AppData.dat and read it back from the file, one list object at a time. I will use specific error type EOFError (end of file error) as a logical step in a while loop. I found this approach on external website: https://www.kite.com/python/answers/how-to-read-a-pickle-file-in-python

## Step 1
I added heading for my script:
# ------------------------------------------------- #
# Title: Pickling and Exception Handling in Python
# Description: Storing and reading vaccination data for different cities
# ChangeLog: (Who, When, What)
# ElenaMcDonald,05.24.2021,Created script

## Step 2
I imported pickle module:
import pickle  # imports code for pickling functions

## Step 3
I added ‘structure’ placeholders: -----data--------, -----------processing-----------, -----------presentation--------
These will hold my future functions
## Step 4
I named my variables at the top:
strFileName = "AppData.dat"
lstData = []

## Step 5
I wrote functions for pickling and unpickling data:

def save_data_to_file(file_name, list):
    """Using Pickling for storing data in a binary file
    :param file_name: target binary file
    :param list: list of values to be added
    """
    file = open(file_name, "ab")  # append new data to a file
    pickle.dump(list, file)
    file.close()

Figure 4. Pickling

def read_data_file(file_name):
    """Reads all data from binary file and appends it to list of objects
    :param file_name: binary source file (previously pickled)
    :return: list of pickled objects
    """
    # loops through and loads all lists from binary file, until "end of file" exception
    file = open(file_name, "rb")
    list = []
    while True:
        try:
            list.append(pickle.load(file))
        except EOFError:  # "end of file" built-in exception used to break the loop
            break
    file.close()
    return list

Figure 5. Unpickling

## Step 6
I wrote function for collecting user input. This includes 3 examples of exception handling: generic error, specific error type (ValueError) and custom error for entering negative number, as shown in Figure 6:

def input_new_data():
    """Collects user input data for cities and number of people vaccinated
       and stores both variables in a list
    :return: list consisting of 2 values: city and number of people vaccinated
    """
    # need to specify exception types and raise custom exception
    while True:
        try:
            strCity = str(input("Enter city: "))
            intNumber = int(input("People vaccinated: "))
            lstData = [strCity, intNumber]
            if intNumber < 0:  # raising custom exception
                raise Exception("Number of vaccinated people must be >= 0")
            else:
                return lstData
        except ValueError as e:  # catching errors related to non-int values entered
            print("Please enter only numeric values for people vaccinated! ")
        except Exception as e:  # this exception catches all the rest
            print("There was a non-specific error!")
            print(e, e.__doc__, type(e), sep='\n')

Figure 5. Examples of using exceptions

## Step 7
At the end I wrote my main() function:

def main():
 while True:
    lstData = input_new_data()
    save_data_to_file(strFileName, lstData)
    print("Data Saved!")
    print("New file contents: ")
    print(read_data_file(strFileName))
    strChoice = input("Add another? Y/N: ")
    if strChoice.lower().strip() == "y":
        continue
    break

![image](https://user-images.githubusercontent.com/84052822/119774119-8ca56500-be76-11eb-91af-69e53247dbfb.png)


## Testing in PyCharm
First, I input my first 2 entries:
 

These were converted to binary format and saved in AppData.dat file:
 
When I rerun program, these entries were ‘unpickled’ – loaded back to memory from the binary file:
 

My third entry was appended to the existing data in the file:
 

Testing in Mac OS Terminal:
I added 2 more cities. Program then saved these entries to binary file (pickled) then unpickled and printed it on the screen together with new entries: 

 

I can see my new entries appended in the newly pickled file: 


 

## Summary
Pickling and unpickling is an easy way to store data using built-in Python functions. Though not always secure, it could be implementing for different use cases, like storing models for machine learning, etc. 
Exception handling is extremely flexible in Python and could be used for a variety of use cases, even as a logic for the loops. 
![image](https://user-images.githubusercontent.com/84052822/119773245-3126a780-be75-11eb-93a1-0e8d0bbd993d.png)
