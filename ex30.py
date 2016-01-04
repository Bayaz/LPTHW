#ex30.py

people = 30
cars = 40
trucks= 15

if cars > people:
	print("We should drive where we are going")
elif cars < people:
	print("We need to walk")
else:
	print("we have just enought cars for everyone")

if trucks > cars:
	print("Thats way more trucks than cars")
elif trucks < cars:
	print("we have more cars than trucks")
else:
	print("we have the same amount of trucks and cars")

if people > trucks:
	print("ok....let's just take the trucks")
else:
	print("fine....lets stay home then")