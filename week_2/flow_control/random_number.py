"""
	Random Number Simulator
		- User guesses a number between 1 and 10
		- User only has five chances
"""

import random

print("Guess a number. You only have five attempts")

attempts = 0

while attempts < 5:
	number = random.randint(1,5)

	userInput = int(input(f"Attempt {attempts + 1}: "))

	if userInput == number:
		print("You WON")
		break
	else:
		print("You LOST")
	attempts += 1