def gallons_to_liters(gallons):
    return gallons*3.785

gallons = float(input("Enter a volume in American gallons (negative value to quit): "))
while (gallons >= 0):
    result = gallons_to_liters(gallons)
    print(f"{gallons:.1f} American gallons is {result:.2f} liters.")
    gallons = int(input("Enter a volume in American gallons (negative value to quit): "))
else:
    print("Program finished.")