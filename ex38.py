ten_things = 'Apples Oranges Crows Telephone Light Sugar'

print("Those are not 10 things...")

stuff = ten_things.split(' ')
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding:", next_one)
    stuff.append(next_one)
    print("Current count:", len(stuff))

print("There we go:", stuff)

print("Lets do some things")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:6]))
print(' / '.join(stuff[0:5]))
