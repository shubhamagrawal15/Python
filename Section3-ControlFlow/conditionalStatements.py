#conditional statements

## if statement
age=20
if(age>=18):
    print("You are allowed to vote in the election.")


## else
## the else statement is used to execute a block of code when the if condition is false
age=16
if(age>=18):
    print("You are allowed to vote in the election.") 
else:
    print("You are not allowed to vote in the election. you are too young.") 
    


## elif
## the elif statement is used to check multiple conditions stands for "else if"

age=20
if(age<13):
    print("You are a child.")
elif(age<18):
    print("You are a teenager.")
else:
    print("You are an adult.")  
    
    
## nested conditional statements

# We can use if statements inside another if statement

num=int(input("Enter a number: "))

if num>0:
    print("The number is positive.")
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is not positive.")
    if num == 0:
        print("The number is zero.")
    else:
        print("The number is negative.")
        
        
## Practical Examples

# Determine if a year is a leap year using nested if statements

year = int(input("Enter a year: "))

if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
  
  
  # Simple calculator using if, elif, and else
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))    
operation = input("Enter operation (+, -, *, /): ") 
if operation == '+':
    print(f"The result is: {num1 + num2}")
elif operation == '-':
    print(f"The result is: {num1 - num2}")
elif operation == '*':
    print(f"The result is: {num1 * num2}")
elif operation == '/':
    if num2 != 0:
        print(f"The result is: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")

# Check if a number is prime using nested if statements
num = int(input("Enter a number: "))     
is_prime = True
if num > 1: 
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")