# operators


# Arithmetic Operators# +, -, *, /, //, %, **

a=10
b=15

add_result = a + b  # Addition
sub_result = a - b  # Subtraction 
mul_result = a * b  # Multiplication
div_result = a / b  # Division  
floor_div_result = a // b  # Floor Division
mod_result = a % b  # Modulus (Remainder)
exp_result = a ** b  # Exponentiation

print("Addition:", add_result)  # Output: 25
print("Subtraction:", sub_result)  # Output: -5    
print("Multiplication:", mul_result)  # Output: 150
print("Division:", div_result)  # Output: 0.6666666666666666
print("Floor Division:", floor_div_result)  # Output: 0
print("Modulus:", mod_result)  # Output: 10
print("Exponentiation:", exp_result)  # Output: 1000000000000000


print(10/5)
print(21/5) # Output: 4.2
print(21//5) # Output: 4


# Comparison Operators# ==, !=, >, <, >=, <=

# ==

a=10
b=10
print(a == b)  # Output: True, because a is equal to b
print(a != b)  # Output: False, because a is not different from b

str1="shubham"
str2="shubham"
print(str1 == str2)  # Output: True, because str1 is equal to str2
print(str1 != str2)  # Output: False, because str1 is not different

#Not equal to
print(a != b)  # Output: False, because a is equal to b
print(str1 != str2)  # Output: False, because str1 is equal to

str3="Krish"
str4="krish"
print(str3 != str4)  # Output: True, because str3 is not equal to str4 (case-sensitive)




# greater than and less than
num1=45
num2=55

print(num1 > num2)  # Output: False, because 45 is not greater than 55
print(num1 < num2)  # Output: True, because 45 is less than 55

# greater than or equal to and less than or equal to
num3=45
num4=45
print(num3 >= num4)  # Output: False, because 45 is not greater than or equal to 55
print(num3 <= num4)  # Output: True, because 45 is less than or equal to 55

# Logical Operators# and, or, not

#and
x=True
y=True
print(x and y)  # Output: True, because both x and y are True

x=False
y=True  
print(x and y)  # Output: False, because x is False


#or
x=True    
y=False
print(x or y)  # Output: True, because at least one of x or y is True

x=False
y=False 
print(x or y)  # Output: False, because both x and y are False


#not
x=True
print(not x)  # Output: False, because not True is False
y=False 
print(not y)  # Output: True, because not False is True

