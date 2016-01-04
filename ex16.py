#ex16.py

#Helpful Read & Write Commands
# close -- Closes the file. Like File->Save.. in your editor.
# read -- Reads the contents of the file. You can assign the result to a variable.
# readline -- Reads just one line of a text file.
# truncate -- Empties the file. Watch out if you care about the file.
# write('stuff') -- Writes "stuff" to the file.

from sys import argv

script, filename = argv

print("we are going to erase: %r" % (filename))
print("if you don't want that hit CTRL C (C^)")
print("if you do want that hit RETURN")
input("?, ")

print("opening the file...")
target = open(filename, 'w')

print("truncating the file")
target.truncate()

print("now I'm going to ask for three lines to populate the file")
# this is what will be written to the text file
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("now I'm going to write these to these to the file...")
#"\n" returns a new line...if not would all be on the same line
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.write("%s\n%s\n%s\n" % (line1, line2, line3))



print("and now finally we close it")
target.close()




