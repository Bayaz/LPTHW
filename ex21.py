#ex21

def add(a, b):
	print("add %d + %d" % (a, b))
	return a + b

def subtract(a, b):
	print("subtract %d - %d" % (a, b))
	return a - b

def multiply(a, b):
	print("muliply %d * %d" % (a, b))
	return a * b


def divide(a, b):
	print("divide %d / %d" % (a, b))
	return a / b

print("let's do some math with just functions")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("age is %d, and I'm %d inches tall, and weigh %d lbs, and my iq is %d" % (age, height, weight, iq))


print("here is a puzzle....")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("that becomes", what, "can you do it by hand")

