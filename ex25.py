# !!! first definition must be run or 'words' must be manually definied before other functions will work!!!

#instead of 'import ex25' you can type 'from ex25 import *' and won't have to type ex25. before functions

# this taught me the lesson of after importing calling the file
# in interpreter write ex25.break_words(sentence)
# this also taught me to utilize the same number of variable as are in the function

# here is how to run the following from the commmand line
# $ python
# >> import ex25
# >> variable_one = "this is the first variable or argument required in break_words function"
# >> variable_two = ex25.break_words(variable_one)
# >> variable_two
# ['this', 'is, the', 'first', 'variable', etc...]

def break_words(stuff):
    """ This function will break up words for us. """
    words = stuff.split(' ')
    return words

# this function without the above splitting the words returns the letters and spaces of a string sorted alphabetically 
# spaces first
def sort_words(words):
	"""sorts the words"""
#doesn't nee words to be set within function because it already is set by previous break_words fuction
	return sorted(words)

def print_first_word(words):
	"""prints the first word after popping it off"""
	word = words.pop(0)
	print(word)

def print_last_word(words):
	"""prints the last word """
	word = words.pop(-1)
	print(word)

def sort_sentence(sentence):
	"takes in a full sentence and returns the sorted words"
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""prints first and last words of sentence"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""prints the first and last words of the sorted sentence"""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)