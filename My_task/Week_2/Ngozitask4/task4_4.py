user_name = input("Enter your names:")
user_names = user_name.lower().split()
for user_name in user_names:
    user_names.sort()
    print(f"{user_name}\n")