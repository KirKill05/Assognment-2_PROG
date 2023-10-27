import random

print("Welcome to Programming Principles Sample Product Inventory")
pr_code = int(input("Please enter the Product Code: "))
pr_name = input("Please enter the Profuct Name: ")
cr_stock = int(input("Please enter the Currect Stock: "))
pr_price = float(input("Please enter the Product Sale Price: "))
pr_manufacture_cost = float(input("Please enter the Produc Manufacture Cost: "))
montly_production = int(input("Please enter estemated monthly production: "))
print("")
print("*******Programming Principles Sample Stock Statement*******\n")
print("Product Code:", pr_code)
print("Product Name:", pr_name, "\n")
print("Sale Price:", pr_price, "CAD")
print("Manufacture Cost:", pr_manufacture_cost, "CAD")
print("Monthly production:", montly_production, "units (approx.)")

month = 1
total_manif = montly_production * 12
total_sold = 0
while month != 12:
    print("Month:", month)
    print("    Manifactured:", montly_production)
    selling = montly_production + random(-10, 11)
    total_sold += selling 
    print("    Sold:",  selling)
    cr_stock = montly_production + cr_stock - selling
    print("    Stock:", cr_stock)
    month += 1

if month == 12:
    print("Net Profit:", (total_sold * pr_price) - (total_manif * pr_manufacture_cost), "CAD")