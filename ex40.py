#ex40.py Classes & OOP
# self - Inside the functions in a class 'self' is a variable representing the instance being accessed
# there are two!! _ in int.... __init__ not _init_!!

class Song(object):
#self doesn't have to be called self to work... the first variable passed in __init__ will act as self or instance of that object
	def __init__(self, y):
			self.y = y

	def sing_me_a_song(self):
			for thing in self.y:
				print(thing)

#these songs are lists...so the object we are inserting happens to be a list...
happy_bday = Song(["Happy Birthday to you", 2 , 'printing last part of list'])

#placing a song as a list
bulls_on_parade = Song(["They rally round your family"])

#print([ "Happy Birthday to you",
#		"I don't want to get sued",
#		"So, I'll stop right there"])


happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

