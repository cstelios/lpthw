#Simple print line. Prints a string:
print("I will now count my chickens:")

#Prints a string and subsequently divides 30 by 6 and adds the result (5.0),
# to 25 giving the result: 30.0.
#It seems the division turns the variable to a floating point number
print("Hens", 25.0 + 30 / 6)
#Prints a string and subsequently multiplies 25 times 3 (75)
#then divides 75 by 4 and returns the remainder which is 3
# subtructs 3 from 100 and returns 97
print("Roosters", 100.0 - 25 * 3 % 4)

#Prints a string
print("Now I will count the eggs:")

# Step 1. 4 % 2 returns 0 since there 4 is divisible by 2 exactly
# Step 2. 1 / 4 return 0.25
# Step 3. Solve (3 + 2 + 1 - 5 + 0 - 0.25 + 6) = 6.75
#                  5   +  -4   +  -0.25   + 6
#                      1       +      5.75
print(3.0 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

# Prints string
print("Is it true that 3 + 2 < 5 - 7?")

# Calculates 3 + 2 (5) and 5 - 7 (-2) and returns True if 5 is smaller than -2 and false if it is not. It will return False
print(3.0 + 2 < 5.0 - 7)

print("What is 3 + 2?", 3.0 + 2)
print("What is 5 - 7?", 5.0 - 7)

print("Oh, that's why it's False.")

print("How about some more.")


print("Is it greater?", 5.0 > -2.0)
print("Is it greater or equal?", 5.0 >= -2.0)
print("Is it less or equal?", 5.0 <= -2.0)
