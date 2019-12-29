def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

def puzzle(a, b, c, d):
    return add(a, subtract(b, multiply(c, divide(d, 2))))

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

stringToPrint = "Age: {}, Height: {}, Weight: {}, IQ: {}"
print(stringToPrint.format(age, height, weight, iq))

# A puzzle for extra credit, type it anyway.
print("Here is a puzzle.")

what = puzzle(age, height, weight, iq) #add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
