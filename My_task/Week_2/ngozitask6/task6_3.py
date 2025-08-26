#task 3: Stimulate a football match ticket system
seat_numbers = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,42,43,44,45,46,47,48,49,50}
print("enter your seat numbers")
user_1 = int(input("Enter your seat number  "))
user_2 = int(input("Enter your seat number :"))
user_3 = int(input("Enter your seat number :"))
user_4 = int(input("Enter your seat number :"))
user_seat_number = {user_1, user_2, user_3, user_4}
seat_numbers.remove(user_1)
seat_numbers.remove(user_2)
seat_numbers.remove(user_3)
seat_numbers.remove(user_4)
print(seat_numbers)


