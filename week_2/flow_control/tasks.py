
"""
1.Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
 You are given n  scores. Store them in a list and find the score of the runner-up.

The first line contains n . The second line contains an array A[]  of n integers each separated by a space.

Sample input

5
2 3 6 6 5
Sample output

5

"""

# scores = int(input("Enter Score"))

# listScores = [10,2,42,42,30,46,5,5,63,63]

# results = []


# for i in listScores:
# 	if i not in results: # Condition to check if the value i
# 		results.append(i)

# print(results)

# results.sort()
# print(results)
# print(results[-2])


"""
2.Given an integer n, perform the following conditional actions:

If n is odd, print Weird
If n  is even and in the inclusive range of 2 to 5 , print Not Weird
If n  is even and in the inclusive range of 6  to 20, print Weird
If n  is even and greater than 20, print Not Weird

Input format

A single line containing a positive integer.

Sample input

3
Sample output

Weird

"""


# n = int(input("Enter an Integer: "))

# if n%2 != 0:
# 	print("Weird")
# elif (n%2 == 0) and (5 >= n >= 2):
# 	print("Not Weird")
# elif (n%2 == 0) and (20 >= n >= 6):
# 	print("Weird")
# elif (n%2 == 0) and (n > 20):
# 	print("Not Weird")
# else:
# 	print("Invalid")


"""
3.Read an integer N . For all non-negative integers , print i2 . See the sample for details.

Input format

The first and only line contains the integer, N.

Sample input

5
Sample output

0
1
4
9
16

"""	
# While Loop

userInput = int(input("Enter Number: "))

i = 0
while i < userInput:
	print(i ** 2)
	i += 1

# For Loop

input = int(input("Enter Number: "))

if input > 0:
	for i in range(0,input):
		print(i ** 2)
else:
	print("Negative Number")