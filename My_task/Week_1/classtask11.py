# Task 11 :Nigerian Currency converter
amount_in_naira = float(input("Enter the amount in Naira: "))
Exchange_rate_US = float(input("Enter the Exchange rate to US dollar (#per $1):"))
Exchange_rate_Brtish= float(input("Enter the Exchange rate to British pounds (# per £1):"))
amount_in_usd = amount_in_naira/Exchange_rate_US
amount_in_bp = amount_in_naira/Exchange_rate_Brtish 
print("\n===== Currency Coversion ======")
print(f"Amount in Naira: #{amount_in_naira:,.2f}")
print(f"Enter the exchange rate in US dollars: ${amount_in_usd:,.2f}")
print(f"Enter the Exhange rate to British pounds: £{amount_in_bp:,.2f}")
print("=======================================")