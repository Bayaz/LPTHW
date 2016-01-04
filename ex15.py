#ex15.py reading files

from sys import argv

script, filename = argv

txt = open(filename)

print(script)

print("Here's your file: %r and here is your script: %r " % (filename, script))

print(txt.read())

print("type the filename again")

#allows for input of filename to be opened again
#main difference is argv method is called initially which may be faster
#input is good if you require input in the program

file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())


#good practice to close the files
txt.close()

txt_again.close()






