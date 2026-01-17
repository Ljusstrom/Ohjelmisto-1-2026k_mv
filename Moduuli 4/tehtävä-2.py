value = float(input("Enter length in inches (negative value to quit): "))
while (value >= 0):
    print(f"{value} inches is {value*2.54:.2f} centimeters")
    value = float(input("Enter length in inches (negative value to quit): "))
print("Program ended.")