#input
# This code prompts the user to enter their age and then prints it.


age=input("Enter your age: ")
print(age)
print(type(age))  # Output: <class 'str'>, since input() returns a string 
# Note: The input is always taken as a string, so you may need to convert it to an integer if necessary.


age=int(input("Enter your age: "))
print(age)  # Output: The age entered by the user
print(type(age))  # Output: <class 'int'>, after conversion to integer  



## simple Calculator
# This code performs basic arithmetic operations based on user input.

num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))

sum_result=num1 + num2
diff_result=num1 - num2 
prod_result=num1 * num2 
div_result=num1 / num2 if num2 != 0 else "Division by zero is not allowed"

print(sum_result)  # Output: Sum of num1 and num2
print(diff_result)  # Output: Difference of num1 and num2         
print(prod_result)  # Output: Product of num1 and num2
print(div_result)  # Output: Division of num1 by num2 or an error message 