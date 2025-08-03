#tuple
#definition 

#creating a tuple
empty_tuple=()
print(empty_tuple)
print(type(empty_tuple))


lst = list()
print(type(lst))

# list  into tuple
numbers=tuple([1,2,3,4,5,6])
print(numbers)

# tuple into list
numbers=list((1,2,3,4,5))
print(numbers)


mixed_tuple=(1,"heelo",3.14,True)
print(mixed_tuple)


#Accesing tuple elements

numbers=(1,2,3,4,5,6)
print(numbers[0]) 
print(numbers[-1]) 
print(numbers[0:4])

# Tuple Operations

# concatination of tuple
print(numbers+mixed_tuple)


print(mixed_tuple*3) # entire tuple got repeated three times
print(numbers*3)


#Immutable nature of tuples

lst = [1,2,3,4,5]
print(lst)
lst[1]="shubham"
print(lst)

# numbers[1]="shubbam"
# print(numbers)


## tuple methods
print(numbers)
print(numbers.count(1))
print(numbers.index(3))


#packing and unpacking tuple

packed_tuple =1,"heelo",3.14
print(packed_tuple)


# unpacking a tuple
a,b,c=packed_tuple
print(a)
print(b)
print(c)

# unpacking with star

numbers=(1,2,3,4,5,6)
first,*middle,third = numbers
print(first)
print(middle)
print(third)


# Nested List

lst=[[1,2,3,4],[6,7,8,9],[1,"heelo",3.14,"c"]]
print(lst[0][1])


lst1=[[1,2,3,4],[6,7,8,9],(1,"heelo",3.14,"c")]
print(lst1[2][0:3])



#Nested Tuple

nested_tuple=((1,2,3),("a","b","c"),(True,False))

## accessing the elements inside a tuple

print(nested_tuple[0])
print(nested_tuple[1][2])


# iterating over nested tuples

for tuple in nested_tuple:
  for element in tuple:
    print(element,end=" ")
  print()
