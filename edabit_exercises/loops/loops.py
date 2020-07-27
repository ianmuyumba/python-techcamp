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
num = 1

def factorial(num):
	if num == 0 or num == 1:
		return 1
	elif num > 1:
		return num * factorial(num-1)
	else:
		return None

num = int(input("Enter Positive Integer: "))
ans = factorial(num)
print(ans)