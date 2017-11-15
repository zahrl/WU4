class Person:
	def __init__(self, name):
		self.name = name
	def talk(self): # abstract
		raise NotImplementedError("Subclass must implement abstract method")

class Student(Person):
	def talk(self):
		return "Let's talk"