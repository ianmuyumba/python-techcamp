"""
	Functions
	- Group of related statements that perform a specific task
	- Useful in organizing code into smaller and modular chunks
	- As our program grows larger and larger, functions make it more
	organized and manageable.
	- Further more, we practice the concept of DRY(DON'T REPEAT YOURSELF), ie
	you can reuse a function in another file in your project
		
		TYPES

		1.in-built functions - This types of functions come with the standard python library.
		Some of the most used in build functions include print(), len(), eval(), count().... etc
		2.user defined functions - Python allows us to define our own functions,
		which perform a specific purpose.

		SYNTAX

		def function_name(parameters):
			# docstring - to describe what the function does
			statement(s) - must have the same indentation level

"""

# def myFunction():
# 	# Simple Function - Docstring to state what the function does
# 	print("My Function")

# myFunction()


# # Function that takes in parameters
# def addNumbers(a,b):
# 	# Add two integers
# 	return a+b

# sum = addNumbers(10,5)
# print(sum)




# def totalMarks(maths, english, kiswahili):
# 	#Get total marks
# 	return maths+english+kiswahili

# total = totalMarks(80,80,80)
# print(total)


# print("Enter Marks")
# maths = int(input("Maths: "))
# english = int(input("English: "))
# kiswahili = int(input("Kiswahili: "))

# total = totalMarks(maths,english,kiswahili)
# print(total)



# Python default parameters

def greetUser(name, message = "Niaje"): # Default parameter parsed in for the second parameter
	# Take in name input and print greetings message
	print(f"{name} {message}")

name = input("Name: ")
greetUser(name)












































#Python