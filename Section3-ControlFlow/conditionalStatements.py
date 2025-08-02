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
  