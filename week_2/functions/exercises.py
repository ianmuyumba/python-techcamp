# 1. Create a function that takes a name and returns a greeting

# def greeting(name):
# 	# Take name and return greeting
# 	print(f"Hello {name}!")

# name = input("Enter Name: ")

# greeting(name)

# 2. Write a function that takes the base and height of a triangle and return its area.

# def areaTriangle(base,height):
# 	# Area of a triangle
# 	# Area = ((0.5*base)*height)
# 	return ((base/2)*height)

# base = int(input("Base: "))
# height = int(input("Height: "))

# area = areaTriangle(base,height)
# print(area)




# 3. Create a function that finds the maximum range of a triangles third edge
		# maximum range of third edge = (side1 + side2) - 1

# def nextEdge(side1,side2):
# 	# Max range of third age ((side1 + side2) - 1)
# 	return (side1 + side2) - 1

# side1 = int(input("Side 1: "))
# side2 = int(input("Side 2: "))

# next_edge = nextEdge(side1,side2)
# print(next_edge)



# 4. Create a function that takes a list and returns the first element

# print("Enter five numbers into the list")

# myList = []

# num = 0

# while num < 5:
# 	userNumber = int(input(f"Enter Number {num + 1}: "))
# 	myList.append(userNumber)
# 	num += 1

# def firstElement(myList):
# 	return myList[0]

# first_value = firstElement(myList)
# print(first_value)






# 5. You've got chickens (2 legs), cows (4 legs) and pigs (4 legs) on your farm.
	# Return the total number of legs on your farm. (CREATE A FUNCTION)

# def number_of_legs(chickens,cows,pigs):
# 	return (chickens*2) + (cows*4) + pigs*4


# animals = number_of_legs(2, 3, 5)
# print(animals)






# 6. Create a function that takes a list of numbers.
	# Return the largest number in the list.

# print("Enter five numbers to be appended to your list")

# listNumbers = []

# num1 = 0

# while num1 < 5:
# 	num2 = int(input(f"Number {num1 + 1}: "))
# 	listNumbers.append(num2)
# 	num1 += 1

# def list_of_numbers(listNumbers):
# 	listNumbers.sort()
# 	return listNumbers[-1]

# largestNumber = list_of_numbers(listNumbers)
# print(largestNumber)


# 7. Given a list of integers, return the difference between the largest and smallest integers in the list.


# print("Enter five numbers to be appended to your list")

# listNumbers = []

# num1 = 0

# while num1 < 5:
# 	num2 = int(input(f"Number {num1 + 1}: "))
# 	listNumbers.append(num2)
# 	num1 += 1

# def list_of_numbers(listNumbers):
# 	listNumbers.sort()
# 	return listNumbers[-1] - listNumbers[0]

# largestNumber = list_of_numbers(listNumbers)
# print(largestNumber)





# 8. Create a function to concatenate two integer lists

# def concat(mylist1,mylist2):
# 	return mylist1 + mylist2

# concatenated_list = concat([1, 3, 5], [2, 6, 8])
# print(concatenated_list)





"""
	# 9. Create a function that takes two strings as arguments and return either True or False
	depending on whether the total number of characters in the first string is equal to the
	total number of characters in the second string
"""



# string1 = input("String 1: ")
# string2 = input("String 2: ")

# def lengthString(string1,string2):
# 	if len(string1) == len(string2):
# 		return True
# 	else:
# 		return False

# result = lengthString(string1,string2)
# print(result)


"""
j)Write a function that converts a dictionary into a list, where each element represents a key-value pair.

example:

convert_to_array({ "a": 1, "b": 2 }) ➞ [["a", 1], ["b", 2]]

convert_to_array({ "shrimp": 15, "tots": 12 }) ➞ [["shrimp", 15], ["tots", 12]]

convert_to_array({}) ➞ []

"""

# Method 1
def dictionaryList(myDictionary):
	newList = []

	for i in myDictionary.items():
		newList.append(list(i))
	return newList

print(dictionaryList({ "a": 1, "b": 2 }))


# Method 1
def dictionaryList(myDictionary):
	newList = []

	for key, value in myDictionary.items():
		newList.append([key,value])
	return newList

print(dictionaryList({ "a": 1, "b": 2 }))


"""
You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product. You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), and the starting inventory. Return the total profit made, rounded to the nearest dollar. Assume all of the inventory has been sold.

example:

profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}) ➞ 14796

profit({
  "cost_price": 225.89,
  "sell_price": 550.00,
  "inventory": 100
}) ➞ 32411

profit({
  "cost_price": 2.77,
  "sell_price": 7.95,
  "inventory": 8500
}) ➞ 44030


NOTE:Profit = Total Sales - Total Cost

"""














# testDictionary = {}
# newList = []

# def dictionaryList(testDictionary):
# 	for key, value in testDictionary.items():
# 		newList.append([key] + val) 


# myList = dictionaryList({ "a": 1, "b": 2 })
# print(myList)























# Python