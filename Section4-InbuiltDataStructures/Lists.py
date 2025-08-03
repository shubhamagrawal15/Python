#Lists
# Lists are ordered collections of items that can be of different types.
# They are mutable, meaning you can change their content after creation.


# creating a list

lst=[1,2,3,4,5,6,7,8,9,10]

print(type(lst))  # Output: <class 'list'>  
print(lst)         # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Accessing elements in a list
print(lst[0])     # Output: 1 (first element)     
print(lst[1])     # Output: 2 (second element)
print(lst[-1])    # Output: 10 (last element) 
print(lst[-2])    # Output: 9 (second last element) 

names=["Alice", "Bob", "Charlie", "David"]
print(names)  # Output: ['Alice', 'Bob', 'Charlie', 'David']

mixed_list = [1, "Hello", 3.14, True]
print(mixed_list)  # Output: [1, 'Hello', 3.14, True] 


#accessing elements in a list

fruits=["apple", "banana", "cherry", "kiwi","guava"]

print(fruits[0])  # Output: apple (first element)
print(fruits[1])  # Output: banana (second element)
print(fruits[-1]) # Output: guava (last element)
print(fruits[-2]) # Output: kiwi (second last element)

# Slicing a list
print(fruits[1:3])  # Output: ['banana', 'cherry'] (elements from index 1 to 2)
print(fruits[:2])   # Output: ['apple', 'banana'] (elements from start to index 1)
print(fruits[2:])   # Output: ['cherry', 'kiwi', 'guava'] (elements from index 2 to end)
print(fruits[-3:])  # Output: ['cherry', 'kiwi', 'guava'] (last three elements)
print(fruits[:-2])  # Output: ['apple', 'banana', 'cherry'] (all but the last two elements)


# Modifying a list
fruits[0] = "orange"  # Change the first element    
print(fruits)  # Output: ['orange', 'banana', 'cherry', 'kiwi', 'guava']

fruits.append("mango")  # Add a new element at the end
print(fruits)  # Output: ['orange', 'banana', 'cherry', 'kiwi', 'guava', 'mango']

fruits[1:]="watermelom"
print(fruits)  # Output: ['orange', 'w', 'a', 't', 'e', 'r', 'm', 'e', 'l', 'o', 'm']


fruits=["apple", "banana", "cherry", "kiwi","guava"]


#list methods

fruits.append("orange")  # Add an element at the end
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'kiwi', 'guava', 'orange']

fruits.insert(1,"watermelon")  # Insert an element at index 1
print(fruits)  # Output: ['apple', 'watermelon', 'banana', 'cherry', 'kiwi', 'guava', 'orange']


# removing the first occurrence of an element
fruits.remove("banana")  # Remove the first occurrence of "banana"
print(fruits)  # Output: ['apple', 'watermelon', 'cherry', 'kiwi', 'guava', 'orange'] 

# remove and return the last item
print(fruits.pop())  # Output: orange (removes and returns the last element)


#Index of the fruit

print(fruits.index("kiwi"))  # Output: 3 (index of "kiwi" in the list fruits)

fruits.count("kiwi")  # Output: 1 (count of "kiwi" in the list fruits)

fruits.append("banana")
fruits.append("banana")

print(fruits.count("banana"))  # Output: 1 (count of "banana" in the list fruits)


# Sorting a list
fruits.sort()  # Sort the list in ascending order
print(fruits)  # Output: ['apple', 'banana', 'kiwi', 'watermelon', 'guava', 'orange']

# Reversing a list
fruits.reverse()  # Reverse the order of the list 
print(fruits)  # Output: ['orange', 'guava', 'watermelon', 'kiwi', 'banana', 'apple']


fruits.clear()  # Clear all elements from the list
print(fruits)  # Output: [] (empty list)


#Slicing a list

numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[2:5])  # Output: [3, 4, 5] (elements from index 2 to 4)
print(numbers[:5])   # Output: [1, 2, 3, 4, 5] (elements from start to index 4)
print(numbers[5:])   # Output: [6, 7, 8, 9, 10] (elements from index 5 to end)
print(numbers[::-2])  # Output: [10, 8, 6, 4, 2] (every second element in reverse order)
print(numbers[::2])   # Output: [1, 3, 5, 7, 9] (every second element in original order)
print(numbers[::-1]) # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] (reversed list)



# Iterating through a list

numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
  print(number, end=" ")  # Output: 1 2 3 4 5 6 7 8 9 10 (prints each number in the list) 
  
fruits=["apple", "banana", "cherry", "kiwi","guava"]
for fruit in fruits:  
  print(fruit, end=" ")  # Output: apple banana cherry kiwi guava (prints each fruit in the list) 
  
# Iterating with index
for index, fruit in enumerate(fruits):  
  print(f"Index {index}: {fruit}")  # Output:# Index 0: apple  # Index 1: banana  Index 2: cherry  # Index 3: kiwi  # Index 4: guava  


# List comprehensions

lst=[]
for x in range(10):
  lst.append(x**2)
print(lst)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squared_numbers=[x**2 for x in range(10)]
print(squared_numbers)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# List comprehension has two parts: the expression and the loop.
# The expression is evaluated for each item in the iterable, and the result is collected into a new list.


#syntax:
# Basic syntax: new_list = [expression for item in iterable]

#with condition: new_list = [expression for item in iterable if condition]

evenNumbers=[x  for x in range(10)if x%2==0]
print(evenNumbers)  # Output: [0, 2, 4, 6, 8] (even numbers from 0 to 9)


#basic list comprehension
sqaured_numbers=[x**2 for x in range(30)]
print(sqaured_numbers)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841]

# List comprehension with condition
odd_numbers=[x  for x in range(30) if x%2!=0]
print(odd_numbers)  # Output: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29] (odd numbers from 0 to 29)  

# Nested list comprehension
#syntax: new_list = [expression for item1 in iterable1 for item2 in iterable2 if condition]


lst1=[1, 2, 3, 4]
lst2=['a', 'b', 'c', 'd']

pair=[[i,j]for i in lst1 for j in lst2]
print(pair)  # Output: [[1, 'a'], [1, 'b'], [1, 'c'], [1, 'd'], [2, 'a'], [2, 'b'], [2, 'c'], [2, 'd'], [3, 'a'], [3, 'b'], [3, 'c'], [3, 'd'], [4, 'a'], [4, 'b'], [4, 'c'], [4, 'd']]


# List comprehension with functions calls

words=["hello", "world", "python", "programming"]
lengths=[len(word) for word in words]
print(lengths) # Output: [5, 5, 6, 11] (length of each word in the list)






