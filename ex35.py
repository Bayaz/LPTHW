ten_things = "Apples Oranges Crows Telephone Light Sugar"
print(ten_things)
print("wait....there are not ten things in that list....let's fix that")

stuff = ten_things.split(' ')
print("this is ten_things after .split", stuff)
more_stuff = ["Day", "Night", "Songs", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("adding next one...", next_one)
    stuff.append(next_one)
    print("There are %d items now" % (len(stuff)))

print("There we go: ", stuff)

print("let's do some things with stuff")


print(stuff[1])


print(stuff[-1])

print(stuff.pop())

print(' '.join(stuff))

print('#'.join(stuff[3:5]))
