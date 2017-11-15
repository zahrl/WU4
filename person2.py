class Person:
	def __init__(self, name):
		self.name = name
	def talk(self):
		raise NotImplementedError("Subclass must implement abstract method")

class Student(Person):
	def talk():
		return "P A R T Y"

class Lecturer(Person):
	def talk():
		return "S T U D Y"

print(Lecturer.talk())
print(Student.talk())