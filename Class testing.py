class Person:
	def __init__(self, name, age, address):
		self.name = name
		self.age = age
		self.address = address
        

name = input("Name: ")
age = input("Age: ")
address = input("Address: ")
p1 = Person(name, age, address)
print("Name: " + p1.name, "Age: " + p1.age, "Address: " + p1.address)