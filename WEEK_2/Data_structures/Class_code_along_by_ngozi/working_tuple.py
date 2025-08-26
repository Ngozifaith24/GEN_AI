# #using parentheses()
# fruits= ("apple","banana","cherry")
# print(fruits)

##without Parentheses (tuple packing)
# numbers = 1,2,3
# print(numbers)

# #single-item tuple
# single_item = ("apple",)
# print(single_item)
# print(type(single_item))

# #mine
# my_item = ("guava",)
# print(my_item)
# print(type(my_item))

# #using tuple(constructor)
# fruits_list = ["apple", "banana","cherry"]
# fruit_tuple = tuple(fruits_list)
# print(fruit_tuple)

# #mine
# name_list= ["ife","ngozi", "chioma",]
# name_tuple = tuple(name_list)
# print(name_tuple)


#characteristcs of tuples
#ordered
# colors = ("red", "green", "blue")
# print(colors[0])

# #immutable
# colors = ("red", "green", "blue")
# colors[1] = "yellow"
# print(colors)

# #allow duplicates
# numbers =(1,2,2,3)
# print(numbers)

# #Mixed data types
# mixed = ("apple",3, True, 5.6)
# print(mixed)

#nestd tuples
# nested = (("a", "b",),(1,2))
# print(nested)
# print(nested[0][1])


#Tuple operations
#1.indexing
fruits = ("apple", "banana", "cherry")
print(fruits[1])
print(fruits[-1])
print(fruits[2])

#2. Slicing
print(fruits[0:2])
print(fruits[::-1])

# 3. Concatenation
tuple1 =(1,2)
tuple2 =(3,4)
result = tuple1 + tuple2
print(result)

# 4. Repetition
nums = (1,2)
print(nums*3)

#5. Membership
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)
print("grape" not in fruits)


#6. Iteration
for fruit in fruits:
    print(fruit)

#Unpacking tuples
person = ("John",25,"Nigeria")
name,age,country = person
print(name)
print(age)
print(country)

#Tuple Methods
numbers = (1,2,2,3,4)
print(numbers.count(2)) #this counts the number of times 2 occured
print(numbers.index(3)) #This gives the position of 3

#Converting Between List and Tuple
#Tuple to list
t = (1,2,3)
lst = list(t)
lst.append(4)
print(lst)

#List back to Tuple
t = tuple(lst)
print(t)

#Built-in Function
nums = (4,1,7,3)
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))