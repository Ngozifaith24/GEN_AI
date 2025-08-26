#Python operators
# #COMPARISION OPERATOR
# a =10
# b = 20
# print(a==b) #Using the equal to /false

# print(a!=b) #Using the not equals to / True

# print(a > b) #Using the greater than / #False

# print(a < b) #Using the less than / ##true

# print(a >= 10) #Using greater than or equal to / #True

# print(b <= 25) # Using less than or equal to / #True


# #use case example-student exam result
# score = 75
# print(score >= 50) #True (Passed)
# print(score < 50) #False (Failed)
# print(score ==100) # False (Not full marks)

# #ASSIGNMENT OPERATORS
# x = 10 #Assignment
# print("Inital value:", x)  

# # x += 5 #Adds 5 to x
# print("After x += 5", x)

# # x -= 2 #subtract 2 from x
# print("After x -= 2:", x)

# x *=3 #multiply x by 3
# print("After x *=3:",x)

# x /= 4 #divides x by 4
# print("After x/=4:", x)

# x %= 3 #Stores remainder after division
# print("After x %= 3:", x)

# x = 4 
# x **=2 #Raises x to the power of 2
# print("After x**==2:", x)

# x //=3 #Floor divides x by 3
# print("After x//= 3:", x)

# #use case examples
# balance = 1000
# deposit = 200
# withdraw = 150

# balance += deposit
# balance -= withdraw
# print("Updated Balance:", balance)
# #Output: Updated Balance: 1050

#Logical Operation
# x = 10
# y = 20

# #AND operator
# print(x > 5 and y > 15) #True

# #OR operator
# print(x < 5 or y >15) #True

# #not operator
# print(not(x == 10)) #False

# #Use case example 1 - Scholarship Eligibility
# #Define variables
age = 17
score = 85

#Must be younger than 18 AND Score score above 80
eligible = (age < 18) and (score > 80)
print("Scholarship Eligible:", eligible)
#Output: Scholarship Eligible: True

# Use case examples - Event Access
age =22
has_ticket = False
can_enter =(age >= 18) and(has_ticket or age < 25)
print("Access Granted:", can_enter)