"""
OBJECT ORIENTED PROGRAMMING

"""



class Car:
	# Class Attributes
	model = "Toyota"
	all_wheel = True
	engine_fuel = "Diesel"

	def __init__(self): # Constructor Method - Invoked automatically when you instantiate an object
		print("Invoked")

	# def start_engine(self):
	# 	self.enginestarted = True
	# 	return f"{self.model} {self.make} engine started"

	# def stop_engine(self):
	# 	pass

	# def start_music(self):
	# 	pass

	# def turn_lights_on(self):
	# 	pass

	# def adjust_seats(self):
	# 	pass


car1 = Car()
car2 = Car()
car3 = Car()

# print(type(car1))
# print(type(car2))
# print(type(car3))


# Set an Instance Attribute for car1
car1.make = "Vitz"
car1.seats = 5
car1.color = "Red"

# print(car1.start_engine())


# # Set an Instance Attribute for car2
# car2.make = "Rav4"
# car2.seats = 4
# car2.color = "Blue"


# # Set an Instance Attribute for car2
# car2.make = "Prado"
# car2.seats = 7
# car2.color = "White"


"""
Principles of OOP
	Inheritance
	Abstraction
	Encapsulation
	Polymorphism
"""





















#Python