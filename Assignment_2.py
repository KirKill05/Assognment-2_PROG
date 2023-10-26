import random

print("Welcome to Programming Principles Sample Product Inventory")
pr_code = int(input("Please enter the Product Code: "))
pr_name = input("Please enter the Profuct Name: ")
cr_stock = int(input("Please enter the Currect Stock: "))
pr_price = float(input("Please enter the Product Sale Price: "))
pr_manifacture = float(input("Please enter the Produc Manifacture Cost: "))
montly_production = int(input("Please enter estemated monthly production: "))
print("")
print("*******Programming Principles Sample Stock Statement*******\n")
print("Product Code:", pr_code)
print("Product Name:", pr_name, "\n")
print("Sale Price:", pr_price)
print("Manifacture Cost:", pr_manifacture, "units (approx.)")

month = 1
while month != 12:
    print()