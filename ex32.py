#ex32.py

#Why does for i in range(1, 3): only loop two times instead of three times?
#The range() function only does numbers from the first to the last, not including the last. So it stops at two, not three in the above. 


the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this kind of for loop goes through a list
for number in the_count:
	print("This is number %d" % (number))

# same as above
for fruit in fruits:
	print("A fruit of type: %s" % (fruit))

# we can also go through mixed lists too
for i in change:
	print("I got %r" % (i))

# we can even build lists

elements = []

# then use the range function to count 0 - 5
for i in range(0, 6):
	print("Adding %d to the list" % (i))
	#don't forget append...
	elements.append(i)

for i2 in elements:
	print ("Here is element number %d" % (i2))



