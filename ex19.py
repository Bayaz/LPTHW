#ex19.py

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print("you have %d cheeese" % (cheese_count))
	print("you have %d boxes of crackers" % (boxes_of_crackers))
	print("man, that's enough for a party")
	print("get a blanket \n")

print("we can just give the function numbers directly")

cheese_and_crackers(20, 30)

print("or we can use variables from our script")
cheeses = 19
crackerses = 29

cheese_and_crackers(cheeses, crackerses)

print("we can even do math too")
cheese_and_crackers(4+9, 10+11)

print("and we can combine math and variable too..")
cheese_and_crackers(cheeses + 100 - crackerses * 5, crackerses - 50)
