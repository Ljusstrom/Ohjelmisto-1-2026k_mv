import math

def calculate_unit_price(diameter, price):
    return price / ((diameter/100 / 2) ** 2 * math.pi)

diam = []
price = []
diam.append(float(input("Enter the diameter of the first pizza (cm): ")))
price.append(float(input("Enter the price of the first pizza (euros): ")))
diam.append(float(input("Enter the diameter of the second pizza (cm): ")))
price.append(float(input("Enter the price of the second pizza (euros): ")))

pizza1_unit_price = calculate_unit_price(diam[0], price[0])
pizza2_unit_price = calculate_unit_price(diam[1], price[1])


print(f"Unit price of the first pizza: {pizza1_unit_price:.2f} euros/m²")
print(f"Unit price of the second pizza: {pizza2_unit_price:.2f} euros/m²")
if pizza1_unit_price < pizza2_unit_price:
    print("The first pizza provides better value for money.")
elif pizza1_unit_price < pizza2_unit_price:
    print("The second pizza provides better value for money.")
else:
    print("Pizzas are equal value for money.")