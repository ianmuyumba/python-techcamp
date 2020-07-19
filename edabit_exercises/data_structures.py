"""
Nothing is Nothing?
Given any number of parameters (which is signified using *args syntax), return True if none of the variables are falsy/empty.

"""

# def nothing_is_nothing(*args): # The *args argument allows a function to take any number of parameters
# 	none_bool = True
# 	for arg in args:
# 		if arg == False or arg == None:
# 			none_bool = False
# 			break #Break out of the loop
# 		else:
# 			continue # Continue with the loop
# 	return none_bool


# myVar = nothing_is_nothing(0, False, [], {})
# print(myVar)



"""
To the Power of _____
Create a function that takes a base number and an exponent number and returns the calculation.
"""

def power(base,exponent):
	return base ** exponent

base = int(input("Base: "))
exponent = int(input("Exponent: "))

powerOf = power(5,5)
print(powerOf)


"""

"""




























#Python