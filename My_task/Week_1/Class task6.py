# Task6
name = input("Enter customer's full name:")
units_str = input("enter units consumed (kWh):")
cost_str = input("Enter cost per unit in Naria(#): ")
units = int(units_str)
cost_per_unit = float(cost_str)
total_bill = units * cost_per_unit
receipt = (                                       "=================================\n" "\tELECTRICITY BILL RECIEPT\n"                    "==========================================\n"f"Customer Name :\t{name}\n"f"units Consumed:\t{units}kWh\n"f"cost per Unit:\t#{cost_per_unit:.2f}\n"f"Total Bill:\t#300,000\n"         "======================================")
print(receipt)    