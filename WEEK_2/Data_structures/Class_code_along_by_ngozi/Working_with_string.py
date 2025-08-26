# # # single quotes
# # name = 'Ada'
# # print(name)
# # #Double quotes
# # greeting = "Hello"
# # print(greeting)
# # # Triple quotes (for multi-line string)
# # story = '''Once upon a time,
# # there was a coder named precious.'''
# # print(story)
# # # string with numbers and symbols
# # password = "p@ssw0rd123"
# # print(password)
# # password = '''p@ssw0ord123: 2025'''
# # print(password)
# # # indexing
# # word = "python"
# # print(word[0]) #p
# # print(word[-1]) # n
# # # slicing
word = "python"
# # print(word[0:4])
# print(word[:])
# print(word[0:4])
# print(word[2:])
# print(word[:3])
# print(word[::2])
# print(word[::-1])
print(word[::])
#string concatenation & Repetion
# Concatenation
a = "Hello"
b = "World"
print(a + " " + b)
a = "Ngozi"
b = "faith"
print(a +' ' + b)
#repetion
word = "Hi! "
print(word *3)
#String Searching & Checking 
#Membership
text = "Python programming"
print("Python" in text) #true
print("Java" not in text) #true
#find()/rfind()
text = "Hello World"
print(text.find("o")) # 4
print(text.rfind("o")) # 7

#index()/rindex()
text = "Hello World"
print(text.index("World")) #6


#starswith() / endswith()
filename = "data.csv"
print(filename.startswith("data")) #True
print(filename.endswith(".data")) #True