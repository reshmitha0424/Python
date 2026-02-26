print("hello world!")

# -------PYTHON INTRODUCTION---------
##########################################
# -------PYTHON GET STARTED--------
# Python Installation

# Checking python version 
import sys
print(sys.version)

# In the command prompt, if we type python (or) py, python editor will be opened and it acts as an interpreter 
##########################################
# -------PYTHON SYNTAX--------
# Indentation - very important
# Python uses indentation to indicate a block of code.

# -------PYTHON COMMENTING--------
# Comments start with a #, and Python will render the rest of the line as a comment:

# -------PYTHON STATEMENTS--------
# A computer program is a list of "instructions" to be "executed" by a computer. In a programming language, these programming instructions are called statements.
# Semicolons are optional in Python. You can write multiple statements on one line by separating them with ;

print("hello world")
print("Have a good day")
print("learning python is fun")
##########################################
# -------PYTHON OUTPUT--------
# -------Python text------
# Text in Python must be inside quotes. You can use either " double quotes or ' single quotes:

print("I will", end=" ")
print("print everything on the same line")

# -------Python Numbers------
# we don't put numbers inside double quotes
print(430287)
# You can also do math inside 
print(2+5)
# Text and numbers
print("I am ", 23, "years old")
##########################################
# -------PYTHON COMMENTS--------
print("Hello, World!") #This is a comment
"""
Multi-line comments:
This is a comment
written in
more than just one line
"""
print("Hello, World!")
##########################################
# -------PYTHON VARIABLES--------
# variables are created when you assign a value to it
# has no command for declaring a variable.
x = 5
y = "John"
print(x)
print(y)

#Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4
print(x)
x = "Lucky"
print(x)

# PYTHON CASTING 
# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# GET THE TYPE WITH TYPE() FUNCTION 
print(type(x))

# String variables can be declared either by using single or double quotes

# Variable names are case-sensitive.
a = 2
A = "Two"
print(a, A)

# ------ VARIABLE NAMEs -------
# Multiword variable names - pascal, camel, snake 

# ------ Assign multiple values --------
x, y, z = "Apple", "Orange", "Banana"
print(x, y, z)
x = y =z = "Cherry"
print(x, y, z)
# unpack a collection 
vegies = ["carrot", "potato", "bendi"]
x, y, z = vegies
print(x, y, z)

# ------ Output Variables ------
x = "My name "
y = "is "
z = "Lucky"
print(x+y+z)

x = "5 "
y = "Lucky"
print(x, y)
print(x+y)

# ------ Global variables -------
# Variables that are created outside of a function
# used by everyone, both inside of functions and outside.
# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
# To create a global variable inside a function, you can use the global keyword.
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

def myfunc2():
  print("Python is " + x)
  global y
  y = "nice"

myfunc()
myfunc2()

print("Python is "+ y)
print("Python is "+ x)

##########################################
# -------PYTHON DATA TYPES--------
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

##########################################
# -------PYTHON NUMBERS--------
# int, float, complex, random number
import random

print(random.randrange(1, 10))

##########################################
# -------PYTHON CASTING--------
# assigning a data type 

##########################################
# -------PYTHON STRINGS--------

