#ex29.py

people = 20
cats = 30
dogs = 15

if people < cats:
	print("too many cats we are doomed")

if people > cats:
	print("we will be ok...%d people is more than %d cats" % (people, cats))

if people < dogs:
	print("the world is drooled on")

if people > dogs:
	print("we can pick up the %d poop with no problem" % (dogs))

dogs += 5

print(dogs)

if people >= dogs:
	print("people are greater than or equal to dogs")

if people <+ dogs:
	print("people are less than or equal to dogs")

if people == dogs:
	print("turns out %d dogs is equal to %d people" % (dogs, people))