import os
import time

os.system("clear")

a, b = int(input()), int(input())

for i in range(1, a, 1):
    print("*", end="")

print("*")

for i in range(1, b - 1, 1):
    print("*", end="")
    for i in range(1, a - 1, 1):
        print(" ", end="")
    print("*")

for i in range(1, a + 1, 1):
    print("*", end="")
