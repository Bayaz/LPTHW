#ex20.py
#read() readline() seek() functions are part of standard library
from sys import argv

script, input_file = argv

#changed f to current_file to show intent, arguments can be any variable
#when defining functions variables can be anything
#in this case parameter is f but when called repalce with current_file
# monkeys is just to show when defining functions arguments can be literally anything in definition
def print_all(monkeys):
	print(monkeys.read())

#this uses the seek(0) funtion to go to the beginning (measured in bytes)
def rewind(f):
	f.seek(0)

def middle( f):
	f.seek(1)

#f.readline in this function is is the key TO THIS ENTIRE EXERCISE, current_line is just variable
#printing of lines if coming from readline() function
def print_a_line(line_count, f):
	print(line_count, f.readline())

#this creates a variable for the file that argued when runninning the script (test.txt)
current_file = open(input_file)

print("lets print the whole file \n")


print_all(current_file)

print("now lets rewind like a tape")
rewind(current_file)

print("now lets print out the three lines")
current_line = 1
print_a_line(current_line, current_file)

# current_line += 1 is same as current_line = current_line + 1 on 43 ...just cleaner
current_line += 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)







