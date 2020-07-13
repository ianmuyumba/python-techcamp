"""
    - A program’s control flow is the order in which the program’s code executes.
    - The control flow of a Python program is regulated by conditional statements and loops.
"""

"""
    DECISION CONTROL STRUCTURES
        * if...elif...else
"""

# print("Hello World")

# x: int = 20
# y: int = 10

# if x>y:
#     print(f"{x} is greater than {y}")

# z = int(input("Enter number: "))
#
# if z > 0:
#     print(f"{z} is a positive number")
# else:
#     print(f"{z} is NOT a positive number")
#



# Check if a number is even or odd
#
# num = int(input("Enter Number: "))
#
# # if num%2 == 0:
# #     print(f"{num} is an even number")
# # else:
# #     print(f"{num} is not an even number")
#
# #shorthand option
# print("Even Number") if num%2 == 0 else print("Odd Number")


# num2 = int(input("Enter Number: "))
#
# if num2>0:
#     print(f"{num2} is a positive number")
# elif num2==0:
#     print(f"{num2} is Zero")
# else:
#     print(f"{num2} is a negative number")


# Nested If statements - check if the number is positive or negative or zero
# Indentation is the key in nested statements
#
# num = float(input("Enter a number: "))
#
# if num >= 0: # If the expression is false, the nested statement wont be executed
#     if num == 0:
#         print("Zero")
#     else:
#         print("Positive number")
# else:
#     print("Negative number")
#

"""
    ITERATION CONTROL STRUCTURES
        * for...loop
            Syntax:

                for val in sequence:
                    Body of for

                    N/B
                - Loop continues until we reach the last item in the sequence
                - The body of for loop is separated from the rest of the code using indentation
        * while ...loop
"""

#for...loop

# name = "Ian"
# for char in name:
#     print(char)

# Check for the highest number using nested for loop and if statement
ages = [10,20,30,60,50,40]
highestAge = 0

for age in ages:
    if age > highestAge:
        highestAge = age

print(highestAge)










# Python
