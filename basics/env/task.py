"""
Write a program that takes your full name as input and displays the abbreviations
of the first and middle names except the last name which is displayed as it is.

For example, if your name is Robert Brett Roser, then the output should be R.B.Roser.

"""
firstName = "Robert"
middleName = "Brett"
lastName = "Roser"

print(f"{firstName[0]}.{middleName[0]} {lastName}")
