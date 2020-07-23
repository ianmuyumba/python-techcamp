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
"""
Determine type of variable in taskList using an inbuilt function
"""

# taskList = [23, "Jane", ["Lesson 23", 560, {"currency" : "KES"}], 987, (76,"John")]
# print(type(taskList))


"""
Print KES
"""

# print(taskList[2][-1])

# """
# Print 560
# """

# # print(taskList[2][1])


# """
# Use a function to determine the length of taksList
# """

# # print(len(taskList))

# """
# Change 987 to 789 without using an inbuilt -method (I.e Reverse)
# """

# # taskList[3] = 789 # Modifying a list through direct assignment
# # print(taskList[3])

# """
# Change the name “John” to “Jane”
# """

# # taskList[-1][-1] = "Jane"
# # taskList[-1] = (76, "Jane")
# # print(taskList[-1][-1])
# # print(taskList)

# """
# Find the largest number in ls1 without using the max function.

# """
# # ls1 = [123,34,54645,34,5]

# # ls1.sort()
# # print(ls1[-1])


# """
# # Given the dictionary below, find the total profit made

# 	profit = {
# 	          "cost_price": 32.67,
# 	          "sell_price": 45.00,
# 	          "inventory": 1200
# 	        }
# """
# # totalProfit =  (profit["sell_price"] - profit["cost_price"])* profit["inventory"]

# # print(totalProfit)


# students = {
# 	"name" : "Ian",
# 	"age" : 24,
# 	"class" : 8
# }

# myKeys = students.keys()
# print(myKeys) # Print keys only

# myValues = students.values()
# print(myValues) # Print values only


# for keys,values in students.items(): # Print items from the dictionari in key value pairs
# 	print(f"{keys} : {values}")

# print(students["name"]) # Print value of a specified key



"""
Get Student Names
	-Create a function that takes a dictionary of student names and returns a list of student names in alphabetical order.

		Examples
		get_student_names({
		  "Student 1" : "Steve",
		  "Student 2" : "Becky",
		  "Student 3" : "John"
		})

		➞ ["Becky", "John", "Steve"]

"""

# get_student_names = {
# 		  "Student 1" : "Steve",
# 		  "Student 2" : "Becky",
# 		  "Student 3" : "John"
# 		}

# student_names = get_student_names.values() # Store values in a list
# sorted_student_names = sorted(student_names) # Sort the list of strings alphabetically
# print(sorted_student_names)



# students = {}

# def get_student_names(students):
# 	# students_names = students.values()
# 	sorted_student_names = sorted(students.values())
# 	print(sorted_student_names	)

# get_student_names({
# 		  "Student 1" : "Steve",
# 		  "Student 2" : "Becky",
# 		  "Student 3" : "John"
# 		})



"""
Purge and Organize

	- Given a list of numbers, write a function that returns a list that...

		* Has all duplicate elements removed.
		* Is sorted from least to greatest value.

	Examples
	unique_sort([1, 2, 4, 3]) ➞ [1, 2, 3, 4]

	unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]) ➞ [1, 2, 3, 4]

	unique_sort([6, 7, 3, 2, 1]) ➞ [1, 2, 3, 6, 7]

"""

# myList = [1, 4, 4, 4, 4, 4, 3, 2, 1, 2]

# uniqueList = []

# for i in myList:
# 	if i not in uniqueList:
# 		uniqueList.append(i)

# uniqueList.sort()
# print(uniqueList)



# uniqueList = []

# def unique_sort(lst):
# 	for i in lst:
# 		if i not in uniqueList:
# 			uniqueList.append(i)

# 	uniqueList.sort()
# 	return uniqueList


# Solution
def unique_sort(lst):
  purgedList = []
  for i in sorted(lst):
    if i not in purgedList:
      purgedList.append(i)
  return purgedList
































# Python



























#Python