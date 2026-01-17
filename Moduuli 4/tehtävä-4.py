import random

correct = random.randint(1,10)

value = int(input("Guess a number (1-10): "))
while (value != correct):
    if (int(value) < correct):
        print("Too low")
    if (int(value) > correct):
        print("Too high")
    value = int(input("Guess a number (1-10): "))
print("Correct")
