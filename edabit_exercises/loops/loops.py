"""
	- How Many Vowels?

		* Create a function that takes a string and returns the number (count) of vowels contained within it.

			# Examples
			count_vowels("Celebration") ➞ 5

			count_vowels("Palm") ➞ 1

			count_vowels("Prediction") ➞ 4
			

			# Notes
			a, e, i, o, u are considered vowels (not y).
			All test cases are one word and only contain letters.
"""

# def count_vowels(txt):
#   return sum([1 for x in txt.lower() if x in 'aeiou'])


"""
	- Return the Factorial

		* Create a function that takes an integer and returns the factorial of that integer. That is, the integer multiplied by all positive lower integers.

			# Examples
			factorial(3) ➞ 6
			factorial(5) ➞ 120
			factorial(13) ➞ 6227020800
			
			# Notes
			Assume all inputs are greater than or equal to 0
"""
# num = 1

# def factorial(num):
# 	if num == 0 or num == 1:
# 		return 1
# 	elif num > 1:
# 		return num * factorial(num-1)
# 	else:
# 		return None

# num = int(input("Enter Positive Integer: "))
# ans = factorial(num)
# print(ans)


"""
	- Find the Smallest Number in a List

		Create a function that takes a list of numbers and returns the smallest number in the list.

			# Examples

			find_smallest_num([34, 15, 88, 2]) ➞ 2
			find_smallest_num([34, -345, -1, 100]) ➞ -345
			find_smallest_num([-76, 1.345, 1, 0]) ➞ -76
			find_smallest_num([0.4356, 0.8795, 0.5435, -0.9999]) ➞ -0.9999
			find_smallest_num([7, 7, 7]) ➞ 7
"""
# def find_smallest_num(myList):
# 	myList.sort()
# 	return myList[0]

# find_smallest_num([34, 15, 88, 2])


"""
	- Recursion: Length of a String

		Write a function that returns the length of a string. Make your function recursive.

			# Examples

			length("apple") ➞ 5
			length("make") ➞ 4
			length("a") ➞ 1
			length("") ➞ 0
"""

# def length(txt):
# 	return len(txt)

# lengthTxt = length("apple")
# print(lengthTxt)



"""
	- 25-Mile Marathon

		Mary wants to run a 25-mile marathon. When she attempts to sign up for the marathon,
		she notices the sign-up sheet doesn't directly state the marathon's length. Instead, the marathon's
		length is listed in small, different portions. Help Mary find out how long the marathon actually is.

		Return True if the marathon is 25 miles long, otherwise, return False.

			# Examples

			marathon_distance([1, 2, 3, 4]) ➞ False
			marathon_distance([1, 9, 5, 8, 2]) ➞ True
			marathon_distance([-6, 15, 4]) ➞ True


		Notes

			* Items in the list will always be integers.
			* Items in the list may be negative or positive, but since negative distance isn't possible,
			find a way to convert the sum of the distance into a positive integer.
			* Return False if the arguments are empty or not provided.
"""

# listDistance = []
# listPositiveDistance = []

# def convertNegatives(listDistance):
# 	for i in listDistance:
# 		if i < 0:
# 			i *= -1
# 		listPositiveDistance.append(i)

# 	if sum(listPositiveDistance) == 25:
# 		return True
# 	else: 
# 		return False


# marathon = convertNegatives([1, 9, 5, 8, 2])
# print(marathon)



"""
	- Recursion: Sum

	Write a function that finds the sum of the first n natural numbers. Make your function recursive.

	# Examples
	sum_numbers(5) ➞ 15
	// 1 + 2 + 3 + 4 + 5 = 15
	sum_numbers(1) ➞ 1
	sum_numbers(12) ➞ 78
"""

def sum_numbers(n):
	num = 0
	numbersList = []
	while num <= n:
		numbersList.append(num)
		num += 1

	print(sum(numbersList))

sum_numbers(9)























# Python