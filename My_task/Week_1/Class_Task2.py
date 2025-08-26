# Ask the user for the price of garri per paint 
price_str = input("Enter the price of garri per paint in Naria:")
# covert the sring to a float
price_float = float(price_str)
#Seperate Naria and Kobo parts
naira = int(price_float) #Whole number
kobo = (price_float - naira)*100
print(f"The price of garri per paint is #{naira} and {kobo} Kobo.")