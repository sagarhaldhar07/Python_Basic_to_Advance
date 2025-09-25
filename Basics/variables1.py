# Variables are containers for storing data values.
# Python has no command for declaring a variable.
# A variable is created the moment we first assign a value to it.

x = 5
y = "John"
print(x)
print(y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# If we want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# We can get the data type of a variable with the type() function.

x = 5
y = "John"
print(type(x)) # <class 'int'>
print(type(y)) # <class 'str'>