# ------------------------------------------------- #
# Title: Pickling and Exception Handling in Python
# Description: Storing and reading vaccination data for different cities
# ChangeLog: (Who, When, What)
# ElenaMcDonald,05.24.2021,Created script
# ElenaMcDonald,05.25.2021,Modified script to add examples for exception handling
# ------------------------------------------------- #
import pickle  # imports code for pickling functions

# Data --------------------------------------------- #

strFileName = "AppData.dat"
lstData = []


# Processing --------------------------------------- #
def save_data_to_file(file_name, list):
    """Using Pickling for storing data in a binary file
    :param file_name: target binary file
    :param list: list of values to be added
    """
    file = open(file_name, "ab")  # append new data to a file
    pickle.dump(list, file)
    file.close()


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


# Presentation ------------------------------------- #
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


main()
