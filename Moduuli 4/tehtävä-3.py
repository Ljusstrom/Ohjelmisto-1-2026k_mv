value = input("Enter a number (or press Enter to quit): ")
smallest = 65536
largest = -65536
while (value != ""):
    if (int(value) < smallest):
        smallest = int(value)
    if (int(value) > largest):
        largest = int(value)
    value = input("Enter a number (or press Enter to quit): ")
print(f"Smallest number: {smallest:.1f}")
print(f"Largest number: {largest:.1f}")
