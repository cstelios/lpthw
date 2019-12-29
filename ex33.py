def createNumList(start, end, increment):
    """Takes 3 arguments and creates an incremental list of numbers.
    Arguments:
    1. Start point of the Loop
    2. End point of the loop
    3. Increment value"""

    start = int(start)
    end = int(end)
    increment = int(increment)
    numbers = []

    while start < end:
        print(f"Loop: {start}.")
        numbers.append(start)

        start += increment
        print("Numbers:\n{}".format(numbers))

        print(f"At the bottom i is {start}\n")

    return numbers

def creatCharList(start, end, increment):
    """Takes 3 arguments and creates an incremental list of characters.
    Arguments:
    1. Start point of the Loop
    2. End point of the loop
    3. Increment value"""

    start = int(start)
    end = int(end)
    increment = int(increment)
    characters = []
    i = start

    for i in range(start, end, increment):
        print(f"Loop: {i}.")
        characters.append(chr(i))

        print("Characters:\n{}".format(characters))

        print(f"At the bottom i is {i}\n")

    return characters

def interface():
    choice = input("Hi!\n Characters (1) or Numbers (2)?\n> ")
    start_point, end_point, increment = getVariables()
    if choice == "1":
        characters = creatCharList(start_point, end_point, increment)
        print("The characters:")

        for char in characters:
            print(char)
    elif choice == "2":
        numbers = createNumList(start_point, end_point, increment)
        print("The numbers: ")

        for num in numbers:
            print(num)
    else:
        print("I did not understand that. Please try again.")
        print("Choose \"1\" for a character list and \"2\" for a number list")
        interface()

    choice = input("Create new list?\ny/n\n> ")
    if choice == "y":
        interface()
    else:
        print("Goodbye :)")

def getVariables():
    start = input("Start point? >")
    end = input("End point? >")
    increment = input("Increment? >")
    return (start, end, increment)

interface()
