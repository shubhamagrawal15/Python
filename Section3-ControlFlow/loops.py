#loops

# for loop
#It is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects.

for i in range(5):
    print(i) #Output: 0 1 2 3 4
    
  
for i in range(1,6):
    print(i) #Output: 1 2 3 4 5
    
    
for i in range(1, 11,2):
    print(i) #Output: 1 3 5 7 9
    
    
# step size of -1
#this means it will count down from 5 to 1

for i in range(5, 0, -1):
    print(i) #Output: 5 4 3 2 1
    
for i in range(5, 0, -2):
    print(i) #Output: 5 3 1
    
    
## for loop in a string

string = "shubham"
for char in string:
    print(char)  # Output: s h u b h a m
    
string = "shubham kumar agrawal studies in dypit under the guidance of prof. prashant jadhav"
for word in string:
    print(word)  # Output: s h u b h a m   k u m a r   a g r a w a l   s t u d i e s   i n   d y p i t   u n d e r   t h e   g u i d a n c e   o f   p r o f .   p r a s h a n t   j a d h a v
string = "shubham kumar agrawal studies in dypit under the guidance of prof. prashant jadhav"
for word in string.split():
    print(word)  # Output: shubham kumar agrawal studies in dypit under the guidance of prof. prashant jadhav
    


#while loop
#It is used to execute a block of code repeatedly as long as a given condition is true.

count =0
while count < 5:
    print(count)  # Output: 0 1 2 3 4
    count += 1  
    
count=0
while count % 2==0 and count <= 10:
  print(count) 
  count=count+2
  
  
#break
#The break statement is used to exit a loop prematurely when a certain condition is met.

for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)  # Output: 0 1 2 3 4

print("Loop ended at i =", i)  # Output: Loop ended at i = 5

num=0
while num < 10:
    if num == 5:
        break  # Exit the loop when num is 5
    print(num)  # Output: 0 1 2 3 4
    num += 1
    
#continue
#The continue statement is used to skip the current iteration of a loop and move to the next iteration.   

for i in range(10):
    if i == 5:
        continue  # Skip the iteration when i is 5
    print(i)  # Output: 0 1 2 3 4 6 7 8 9 
print("Loop completed without 5.")

## printing odd numbers using continue
for i in range(0,10):
  if(i%2==0):
    continue
  print(i)
  
  

#pass
#The pass statement is a null operation; it is used when a statement is syntactically required but you do not want to execute any code. It can be useful as a placeholder.

for i in range(5):
  if i==3:
    print("The number is ",i)
    pass
  print(i)
  
  
#nested loop
# it is a loop inside a loop

for i in range(3):
  for j in range(3):
    print(f"i:{i},j:{j}")
    


#Example
#Calculate the sum of natural number using a while loop and for loop

# Using a while loop
n=int(input("Enter a numebr:"))
sum=0
while(n>0):
  sum=sum+n
  n=n-1
print(sum)


# using a for loop
num=int(input("enter the number"))
sum=0
for i in range(0,num+1):
  sum=sum+i
print(sum)



# prime number

for num in range(1,101):
  if num>1:
    for i in range(2,num):
      if num%i==0:
        break
    else:
      print(num)
      
