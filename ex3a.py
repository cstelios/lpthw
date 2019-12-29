import random
import math

x = random.randint(0,10)

print("This program calculates the sum of the first", x, "number of digits of pi")

if x < 1:
    y = 0
elif x < 2:
    y = 3
elif x < 3:
    y = 3 + 1
elif x < 4:
    y = 3 + 1 + 4
elif x < 5:
    y = 3 + 1 + 4 + 1
elif x < 6:
    y = 3 + 1 + 4 + 1 + 5
elif x < 7:
    y = 3 + 1 + 4 + 1 + 5 + 9
elif x < 8:
    y = 3 + 1 + 4 + 1 + 5 + 9 + 2
elif x < 9:
    y = 3 + 1 + 4 + 1 + 5 + 9 + 2 + 6
elif x < 10:
    y = 3 + 1 + 4 + 1 + 5 + 9 + 2 + 6 + 5
elif x < 11:
    y = 3 + 1 + 4 + 1 + 5 + 9 + 2 + 6 + 5 + 3

print("Sum is:", y , "... (pi is equal to", math.pi,")")
