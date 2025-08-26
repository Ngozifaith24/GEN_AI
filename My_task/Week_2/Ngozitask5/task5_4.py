#4
username = input("Enter 5 names seperated by spaces").split()
names = [name.lower() for name in username]
print(*names , sep = "\n")
#4
print("user enter your details")
first_name = input("Enter your first name")
age = input("Enter your age")
Favorite_color = input("Enter your fav color")
Home_town = input("Enter your hometown")
profile= (first_name, age, Favorite_color, Home_town)
print(profile)
print(first_name)
print(age)
print(Favorite_color)
print(Home_town)
print(f"Ngozi profile\n=========================\nFirst name:{first_name}\nAge:{age}\nFavorite color:{Favorite_color}\nHomeTown: {Home_town}\n======================")
