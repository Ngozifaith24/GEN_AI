# #set_in_python
# #1 using curl braces
# fruits = {"apple", "banana","mango"}
# print(fruits)

# #2. using the set() constructor
# numbers = set([1,2,3,4])
# print(numbers)

# #3. Creating an empty set (must use set(), not{})
# empty_set = set()
# print(type(empty_set))

# #4.From a string (duplicates removed automatically)
# # letters = set("mississippi")
# # print(letters)

# #5Set operation
# # #adding elements
# # colors= {"red","blue"}
# # colors.add("green")
# # print(colors)

# # #removing elements
# # colors.remove("blue")
# # colors.discard("yellow")
# # print(colors)

# # #pop an element
# # colors = {"red","blue", "green"}
# # removed = colors.pop()
# # print("Removed:", removed)
# # print("Remaining:", colors)

# # # clear a set
# # colors.clear()
# # print(colors)


# #mathematical set operation
# set1 = {1,2,3,4}
# set2 = {3,4,5,6}

# #1. union
# print(set1 | set2)
# print(set1.union(set2))

# #2. Intersection
# print(set1 & set2)
# print(set1.intersection(set2))

# #3 Difference
# print(set1 - set2)
# print(set1.difference(set2))

# #4 symmetric Differnce
# print(set1 ^ set2)
# print(set1.symmetric_difference(set2))

# #Working with sets

#collecting unique visitors to an event
visitors = set()

#Adding visitors
visitors.add("chinedu")
visitors.add("aisha")
visitors.add("chinedu")
print("Visitors:", visitors)

#checking if a visitor attended
name = "Aisha"
if name in visitors:
    print(f"{name} attended the event.")
else:
    print(f"{name} did not attend the event.")