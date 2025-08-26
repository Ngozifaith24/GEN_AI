# # #range()
# # for i in range(3):
# #     print(i)

# # #zip()
# # names = ["Esther", "Precious", "Kennie"]
# # scores =[85,90, 75]
# # for n,s in zip(names, scores):
# #     print(n, "scored", s)


# # #Map()
# # nums = [1, 2, 3, 4]
# # squared = list(map(lambda x:x**2, nums))
# # print(squared)

# # even_nums = list(filter(lambda x:x % 2==0, nums))
# # print(even_nums)


# # #Student Performance & Feedback system
# # #Step 1: Input student data
# # name1 = input("Enter first student name: ")
# # score1= int(input("Enter score for "+ name1 + ": "))

# # name2 = input("Enter first student name: ")
# # score2= int(input("Enter score for "+ name2 + ": "))

# # name3 = input("Enter first student name: ")
# # score3= int(input("Enter score for "+ name3 + ": "))

# # #Store in list
# # names = [name1, name2, name3]
# # scores = [score1, score2, score3]

# # #Step 3: Display data
# # print("\nStudent Data: ")
# # for index, (n, s) in enumerate(zip(names, scores)):
# #     print(f"{index + 1}. {n} - {s}")

# # #step 4: Summary using built-ins
# # total = sum(scores)
# # average = round(total / len(scores), 2)
# # highest = max(scores)
# # lowest = min(scores)

# # print("\nPerformance Summary:")
# # print("Total Score:", total)
# # print("Average Score:", average)
# # print("Highest Score:", highest)
# # print("Lowest Score:", lowest)

# # #Step 5: Ranking (using sorted and zip)
# # ranked = sorted(zip(scores, names), reverse=True)
# # print("\nRanking:")
# # for rank, (score, name) in enumerate(ranked, 1):
# #     print(f"{rank} . {name} - {score}")


# # #step 6: Check data types
# # print("\nData Type Checks:")
# # print("Type of names:", type(names))
# # print("Type of scores:",type(scores))
# # print("ID of names list:", id(names))
# # print("ID of scores list:", id(scores))

# # # step 7: Filter passing students (>)
# # passing = list(filter(lambda s:s >= 50, scores))
# # print("\nPassing Scores", passing)

# # #step 8: Map names to uppercase
# # upper_names= list(map(lambda n: n.upper(), names))
# # print(upper_names)

# # #step 9: Use help() to show documentation of len
# # print("\nHelp on len():")
# # help(len)

# # defining a function
# def greet():
#     print("Hello, welcome to AI Fellowship!")
# greet()
# greet()
# greet()

# #Function with an arguement - the placeholder
# def greet(name):
#     print("Hello", name, "Welcome to python learning!")

# #Calling with parameter - the actual name
# greet("Class rep")
# greet("Ridwan")


# def greet(name):
#     return f"Hello, {name}"
#     # print("Heollo", name)
# her_name= greet("Esther")

# print("result:", her_name)


# def add(a,b):
#     return a + b

# # Function call
# result = add(4, 6)
# print("The sum is:", result)

# #Note the output and compare it with that of print()

# #yeild
# def count_up_to(n):
#     i = 1
#     while i <= n:
#         yield i
#         i += 1

# #Using the generator
# for number in count_up_to(5):
#     print(number)


# #postional Arguement
# def introduce(name, track):
#     print("My name is", name)
#     print("I am learning", track, ".")
# introduce("ngozi", "Ai engineering")
# introduce("Ai engineering", "Ngozi")

# #Keyword argument
# def introduce(name, track):
#     print("My name is", name)
#     print("I am learning", track,".")

# # function call
# # introduce(name = "Ngozi", track = "AI Engineering")

# # Change the arrangment and watch the output

# introduce(track = "AI Engineering",name = "Ngozi")   # HEre you notice that order does not batter

# #Default Arguement
# def introduce(name, track = "AI Engineering"):
#     print("My name is", name)
#     print("I am learning", track,".")
# introduce("paul")

# introduce("Tunji paul", track = "AI Development")

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Sum:", total)
#Function call
# Take note of the output
add_numbers(2,4,6)
add_numbers(10, 20, 30, 40, 50)   


#Keywords arguement (dictionary)
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

#function call - Take note of the output
student_details(name="Peter", track = "AI Engineering", interest = "Block Chain")

