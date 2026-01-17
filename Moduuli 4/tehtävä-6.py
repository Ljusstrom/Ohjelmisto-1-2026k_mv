import random

N = int(input("Give number of points: "))
n = 0
count = 0
while (count < N):
    n_x = random.random()
    n_y = random.random()
    if (n_x**2 + n_y**2 < 1):
        n+=1
    count += 1
print(f"Approximation of pi: {4*n/N}")