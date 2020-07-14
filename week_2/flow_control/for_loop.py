
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
