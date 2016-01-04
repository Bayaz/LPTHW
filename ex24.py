p41rint("let's practice everything")

print('you\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\t The lovely world
with logic so firmly planted
cannot descern \n the needs of love
nor comprehend passion from intuition
and requires and explanation
\n\t\twhere there is none
"""

print("--------------------")
print(poem)
print("--------------------")

five = 10 - 2 + 3 - 6
print("This should be five: %d" % (five))

#this function simply returns 3 values from 1 input, outside of function the 3 variables can be names anything
# the variables will be assigned in the order typed and all must be used to test delete one 
# of the %d's in the last line of code and run
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 50
	return jelly_beans, jars, crates

start_point = 10000
#this next line is interesting becuse it sets the variable values within the function by calling the function
#they are assigned in order typed and do not have to have the same name...
# so the three variables in the function can be set by just assigning a value to the starting point
beans, jars, crateZ = secret_formula(start_point)

print("we have a starting point of: %d" % (start_point))
print("we have %d beans, %d jars, and %d crates" % (beans, jars, crateZ))

start_point = start_point / 10

print(start_point)

print("we can also do it this way:")
#this is potentially cleaner, you MUST call all three variable or it will error out
print("We'd have %d beans, %d jars, and %d crates" % (secret_formula(start_point)))