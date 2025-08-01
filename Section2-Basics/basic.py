## Case Sensitivity in Python
## This script demonstrates the case sensitivity of Python identifiers.
'''
Welcome to the Python Basics section!

'''
# Python is case-sensitive, meaning that it treats uppercase and lowercase letters as distinct.

# name ="Shubham"
# Name="Shubham2"
# print(name)  # Output: Shubham  
# print(Name)  # Output: Shubham2


#Indentation is also significant in Python, and it is used to define the scope of loops, functions, and classes.
age=32
if age > 30:
    print("You are older than 30 years.") 
    


#LineContinuation allows you to split long lines of code into multiple lines for better readability.
total=1+2+3+4+5+6+7+8+9+10\
    +11+12+13+14+15+16+17+18+19+20
print(total)  # Output: 210
# The backslash (\) at the end of the line indicates that the statement continues on the next line.




#Multlple Statements on a Single Line
# You can write multiple statements on a single line by separating them with semicolons (;).
x = 10; y = 20; z = x + y
print(x, y, z)  # Output: 10 20 30  

# However, this practice is generally discouraged for readability reasons.






#Understanding Sementics
# Python is a dynamically typed language, meaning that you don't need to declare the type of a variable explicitly.
# The type is inferred at runtime based on the value assigned to the variable.

age =32
name="shubham"
print(type(age))   # Output: <class 'int'>
print(type(name))  # Output: <class 'str'>  


variable = 10
# The variable 'variable' is dynamically typed and can hold any type of value.
variable = "Hello, World!"  
print(variable)  # Output: Hello, World!
print(type(variable))  # Output: <class 'str'>  
# This demonstrates the dynamic nature of Python's type system.
# Python also supports multiple assignment, allowing you to assign values to multiple variables in a single line.

## Code example of indentation

if True:
  print("This is indented correctly.")
  if False:
    print("This will not be printed due to the condition.")   
  print("This is also indented correctly.")
print("This is outside the if block and not indented.")  # This line is not indented, so it is outside the if block.