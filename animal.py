class Animal:
	def __init__(self):
		print("Animal created")
	def whoAmI(self):
		print("Animal")
	def eat(self):
		print("Eating")

class Dog(Animal):
	def whoAmI(self):
		print("Dog")
	def bark(self):
		print("Barking")

class Cat(Animal):
	def whoAmI(self):
		print("Cat")
	def meow(self):
		print("Meowing")

c = Cat()
c.whoAmI()
c.eat()
c.meow()