super_market_prices = {} 
items = ["bread","burger", "rice", "garri", "milk"]
super_market_prices["bread"] = input("Enter the price: ")
super_market_prices["burger"] = input("Enter the price: ")
super_market_prices["rice"] = input("Enter the price: ")
super_market_prices["garri"] = input("Enter the price: ")
super_market_prices["milk"] = input("Enter the price: ")
print(f"Bread: {super_market_prices["bread"]}")
print(f"Burger: {super_market_prices["burger"]}")
print(f"Bread: {super_market_prices["rice"]}")
print(f"Bread: {super_market_prices["garri"]}")
print(f"Bread: {super_market_prices["milk"]}")
print("\nAvailable Items: ", list(super_market_prices.keys()))
items
