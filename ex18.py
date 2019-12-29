# This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args

    print(f"arg1: {arg1}, arg2: {arg2}")
# ok that *args was pointless, we can simply do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# This one takes only one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothing")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shawn")
print_one("Stelios")
print_none()
