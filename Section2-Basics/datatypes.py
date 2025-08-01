#datatypes

#definition of a datatype

## Integer
# An integer is a whole number, positive or negative, without decimals.
age=35
print(type(age))

##  Float
# A float is a number that has a decimal point.
height=5.9
print(type(height)) # Output: <class 'float'>

## String
# A string is a sequence of characters enclosed in quotes (single or double).
name="Shubham"
print(type(name))  # Output: <class 'str'>  


## Boolean
# A boolean represents one of two values: True or False.  
is_student = True
print(type(is_student))  # Output: <class 'bool'> 

is_true=bool()
print()


## common errors
result="Hello"+ 5
print(result)  # This will raise a TypeError because you cannot concatenate a string and an integer

result = "Hello" + str(5)  # Correct way to concatenate a string and an integer
print(result)  # Output: Hello5 




