# #Handling errors 
# #SYNTAX ERROR
# #IndentationError - Incorrect spacing
# for i in range(3):
#     print(i)
# # for i in range(3): 
# # print(i) #The indentation error

# # # b Missing Colon/Parenthesis Error
# # if 5 > 3
# # print("Hello")

# # if 5 > 3:
# #     print("Hello") #Corrected one that has the semi colon and indentation

# # #c. Invalid Syntax - General grammar mistakes
# # print "Hello" #Wrong because of no parenthesis

# # print("Hello") # Correct
# #so to fix these things you have to always double check the python grammar, colon, parentheses, and indentation.

# #2. Runtime Errors
# #subtypes of runtime errors
# # a. ZeroDivisionErrors - Dividing by zero.
# # x = 10 / 0
# #b. NameError - Using a variable before defining it.
# print(age) #age is not defined so it cant print

# #c. TypeError - Wrong data type in an operation.

# result = "10"+ 5 #str +int not allowed

# #d. ValueError - invalid value for a function.
# number =int("abc")#cannot convert string to int

# #e. IndexError - Accesing list index out of range 
# fruits = ["apple","banana"]
# print(fruits[3]) #this wil throw error because the  fruits are just 0 and 1 (in positioning)

# #f. KeyError - Accessing a dictionary with a missing key.
# data = {"name": "Ada"}
# print(data["age"]) #this will show Key error because "age has no key value in the variable the information is drawn from"

# #g. FileNotFoundError = File does not exit
# f = open("missing.txt") #file will not be found because it has not been created before

# #How we handle these runtime errors are through provision of exceptions than can prevent the program from crashing
# #these exceptions include a. TRY, b. EXCEPT, c. FINALLY
# #a. try: this is the blockk of code to test for errors. it is used to wrap codes that might raise an error and if no error occurs Python skips the exception block

# try:
#     x= 10 / 2
#     print("Result", x)

# #the Except Block: this is used to define what would be done when a error occurs inside try block and it can catch specigic and all errors 

# #This is a specific exception 
# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Cannot be divived by Zero.")

# #This is a case of multiple exception
# try:
#     number = int("abc") #valueError
#     result = 10 / 0 #ZeroDivisionError
# except ValueError:
#     print("Invalid conversion to integer.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# #The Finally Block :This runs always whether an error occured or not and it is useful for cleanup tasks such as closing files, releasing resources.
# try:
#     f = open("sample.txt", "r")
#     content = f.read()
# except FileNotFoundError:
#     print("File not found.")
# finally:
#     print("Closing file if it was opened.")

# #examples 
# balance = 5000 #starting balance
# print("Welcome to the ATM")
# amount = input("Enter amount to withdraw:")

# try: 
#     amount = float(amount) # convert input to number
#     if amount > balance:
#         raise ValueError("Insufficient funds.")
#     balance -= amount
#     print("Withdrawl sucessful. New balance: ₦", balance)
# except ValueError as e:
#     print("Error:", e)
# except Exception as e:
#     print("Unexpected error:", e)
# finally:
#     print("Transaction session closed")


# #Semantic Errors
# #common Subtypes of sematic errors
# # Wrong Condition in Logic
# age = 18
# if age > 18: #Should be >=
#     print("Eligible to vote")
# else:
#     print("Not eligible")
# #this will give not eligible because the if is asking the program to only accept only from above 18 years instead of >= which would still accept age 18 and above.

# #Wrong Formula/Computation
# length = 10
# width = 5
# area = length + width
# print("Area:", area)
# #output is supposed to be 50 because its meant to be multiplication but addition was used here. Although no error was seen, but it was still wrong

# #Worst variable Usage
# marks = [70,80,90]
# total = marks[0] * marks[1] *marks[2] #This is supposed to be addition not multiplcation
# print("Total:", total)

num1 = int(input("Enter any digit: "))
num2 = int(input("Enter any digit: "))
# try:
div = num1/ num2
# except ZeroDivisionError:
print(div)
    # print("Not allowed")
