#variables
# Variables in Python are used to store data values. They are created when you assign a value to them.
# Variable names can contain letters, numbers, and underscores, but cannot start with a number. 

# Declaring and assigning variables

age = 25  # Integer variable
name = "Alice"  # String variable  
height = 5.5  # Float variable
is_student = True  # Boolean variable

#printing variable values
print(age)  # Output: 25
print(name)  # Output: Alice      
print(height)  # Output: 5.5
print(is_student)  # Output: True

# Naming conventions
# Variable names should be descriptive and follow the naming conventions:
# 1. Use lowercase letters for variable names.
# 2. Use underscores to separate words (e.g., `first_name`, `last_name`).
# 3. Avoid using reserved keywords (e.g., `if`, `else`, `while`, etc.). 
# 4. Use meaningful names that reflect the purpose of the variable.
# 5. Avoid using single-character names except for loop counters or temporary variables.
# 6. Be consistent with naming conventions throughout your code.
# 7. Use CamelCase for class names (e.g., `MyClass`).
# 8. Use all uppercase letters for constants (e.g., `MAX_VALUE`).
# 9. Avoid using special characters or spaces in variable names.
# 10. Use descriptive names that convey the purpose of the variable.

# valid variable names
first_name = "John"
last_name = "Doe"
age_in_years = 30
is_active = True  

# invalid variable names
# 1st_name = "Jane"  # Cannot start with a number   
# last-name = "Smith"  # Hyphens are not allowed
# 2nd_name = "Alice"  # Cannot start with a number
# class = "Math"  # 'class' is a reserved keyword 



#understanding variable types
# Python is a dynamically typed language, meaning you don't need to declare the type of a variable  explicitly. The type is inferred at runtime based on the value assigned to the variable.

age = 32  # Integer
name = "Shubham"  # String  
height = 5.9  # Float
is_student = False  # Boolean

print(type(age))  # Output: <class 'int'>
print(type(name))  # Output: <class 'str'>  


#Conversion between types
age=25
print(type(age))  # Output: <class 'int'>
age_str = str(age)  # Convert integer to string 
print(type(age_str))  # Output: <class 'str'>


age="25"
print(type(age))  # Output: <class 'str'>
age_int = int(age)  # Convert string to integer 


name="shubham"
print(int(name))

height = 5.9
print(type(height))  # Output: <class 'float'>
height_int = int(height)  # Convert float to integer
print(type(height_int))  # Output: <class 'int'>
print(height_int)  # Output: 5



#Dynamic Typing
# Python allows you to change the type of a variable at runtime. This is known as dynamic typing.
variable = 10  # Initially an integer   
variable = "Hello, World!"  # Now a string
print(variable)  # Output: Hello, World!