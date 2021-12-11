#
#=====================================================
# Title: Assignment 8.3 Python in Action
# Author: Gustavo Roo Gonzalez
# Date: 11 December 2021
# Description: Math operations using Python
#=====================================================
#

#Welcome Message
def welcome(name):
    return "Welcome to {} python calculator!".format(name)
print(welcome("Gustavo Roo Gonzalez's"))


# Addition function w/ 2 parameters
def add (a,b):
    return a + b

# Substraction function w/ 2 parameters
def subtract (a,b):
    return a-b

# Division function w/ 2 parameters
def divide (a,b):
    return a/b

# Call each function with a separate print statement 
print('The result of the addition is',add(1,2))
print('The result of the substraction is',subtract(4,1))
print('The result of the division is',divide(8,2))