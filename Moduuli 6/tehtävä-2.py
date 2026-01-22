import random

def roll_dice(sides):
    return random.randint(1,sides)

max_sides = int(input("Give the number of sides: "))
result = 0
while (result != max_sides):
    result = roll_dice(max_sides)
    print(result)
