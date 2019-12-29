from sys import argv

script, filename = argv

print(f"We're goinf to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you want that, hit RETURN")

input("?")

print("Opening the file...")
target = open(filename, 'w+')

print("First, lets check the contents of the file.")
contents = target.read()
print(contents)

print("Are you sure you want to continue? Hit CRTL-C to cancel and RETURN to continue")
input("?")

#target.close()
#print("Opening the file...")
#target = open(filename, 'w+')

print("Truncating the file. Goodbye!")
#target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file")

target.write(f"""
{line1}
{line2}
{line3}
""")

print("And finally, we close it.")
target.close()
