# Printing a python string
print("Hello World")

"""
Indentation refers to the spaces at the beginning of a code line.
Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important. Python uses indentation to indicate a block of code.
"""

if 5 > 2:
  print("Five is greater than two!")

# if 5 > 2:
# print("Five is greater than two!") This will throw error

if 5 > 2:
 print("Five is greater than two!") # minimum one space is allowed
if 5 > 2:
        print("Five is greater than two!") # most commonly four spaces are used

# We have to use the same number of spaces in the same block of code, otherwise Python will give us an error:

"""
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!") Error
"""