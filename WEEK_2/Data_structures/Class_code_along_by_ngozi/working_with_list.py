# # Method 1:Using square bracket
# empty_list = []
# print(empty_list)

# #Method 2: Using the list() constructor
# empty_list2 = list()
# print(empty_list2)

# # List of integers
# numbers = [1, 2, 3, 4, 5]
# print(numbers)

# #list of strings
# fruits = ["apple", "banana", "cherry"]
# print(fruits)

#Mixed data types
# mixed_list = ["Alice", 25,5.8, True]
# print(mixed_list)

# #From a string (each character becomes an element)
# chars = list("hello")
# print(chars)

# #from a tuple
# my_tuple = (10,20,30)
# list_from_tuple= list(my_tuple)
# print(list_from_tuple)

# #From Range
# number_range = list(range(5))
# print(number_range)

# #squares of numbers 0-4
# squares = [x**2 for x in range(5)]
# print(squares)

# #Even numbers between 0-10
# evens = [x for x in range(11) if x % 2==0]
# print(evens)

# #Matrix-like list
# matrix = [[1,2],[3,4],[5,6]]
# print(matrix)

matrix = [[2,4], [6,8, [4,9,3]],[10,12]]
# print(matrix)
# print(matrix[1][2][1])
print(matrix[0][1])






# #Accessing elements in a nested list
# print(matrix[0])
# print(matrix[0][1])

# #Ordered Collection
# fruits = ["mango", "orange", "banana"]
# print(fruits)
# print(fruits[0])
# print(fruits[1])

# #allow duplicates
# items = ["rice", "beans", "yam", "rice"]
# print(items)

#mutable changes
# numbers = [1,2,3,]
# numbers[1] = 20 #changing element at index
# print(numbers)

# #Can Contain
# mixed = [10, "Nigeria",3.14, True]
# print(mixed)

# #can be nested
# nested_list = [[1,2], ["a", "b"]]
# print(nested_list)
# print(nested_list[0][1])

# #Dynamic
# names = ["Ada"]
# names.append("Bola")
# names.append("Chidi")
# print(names)