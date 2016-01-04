#ex31.py

print("You enter a room with 2 doors....\n (1) Do you go through Door Number ONE \n (2) Do you go through door Number TWO")


door = input("> ")

if door == "1":
	print("There is a giant bear eating cheesecke")
	print("(1) Take the cake!")
	print("(2) Scream at the bear")

	bear = input("> ")

	if bear == "1" or "one" or "One":
		print("The bear eats your face off")
	elif bear == "2":
		print("The bear eats your feet off")
	else:
		print("Doing %s was probably a better option" % (bear))

elif door == "2":
	print("You stare into the endless abyss that is Cthulhu")
	print("(1) Bluberries")
	print("(2) Madness")
	print("(3) Revolvers")

	cthulhu = input("> ")

	if cthulhu == "1":
		print("Madness consumes you")
	elif cthulhu =="2":
		print("You dissolve into nothing")
	elif cthulhu == "3":
		print("You slide into insanity")
	else:
		print("You did %s, too bad...still fucked" % (cthulhu))

else:
	print("You stab yourself because of your failure to be able to make simple choices, %s ...what a stupid choice" % (door))

