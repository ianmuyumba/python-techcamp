"""
    - Create an application that asks you to create an account for Jamii Bora APP
        Provide your first name, last name, DOB, email and password

        -------------- WELCOME TO JAMII BORA --------------
        CREATE YOUR ACCOUNT
        Enter your First Name
        Enter your Last Name
        Enter your DOB
        Enter your Email
        Enter your Password

    - After creating the account, it should ask you to login

        -------------- PLEASE LOGIN --------------
        EMAIL ADDRESS:
        PASSWORD:

    - Validate the credentials
    - If all are valid, print "Welcome J.D Peter"
    - Print "Your account balance is 20,000"

"""

print("-------------- WELCOME TO JAMII BORA --------------")
print("CREATE YOUR ACCOUNT")

firstName = input("Enter your First Name: ")
middleName = input("Enter your Middle Name: ")
lastName = input("Enter your Last Name: ")
dob = input("Enter your Date of Birth: ")
email = input("Enter your Email: ")
password = input("Enter your Password: ")

print("-------------- PLEASE LOGIN --------------")
userEmail = input("Email: ")
userPassword = input("Password: ")




if userEmail == email:
    if userPassword == password:
        print(f"Welcome {firstName[0]}.{middleName[0]} {lastName}")
        print("Your account balance is KES 250,000")
    else:
        print("Invalid Password")
else:
    print("Invalid Email")





"""
    - Create a primary school grading system
        Ask for the Student Name, Class, and Score for 5 subjects (Maths, English, Kiswahili, Science, SST)

    OUTPUT

        -------------- RESULTS CARD --------------
        Student Name: Ian Muyumba
        Class: 5
        Total Marks: 400
        Average Score: 80
        Grade: A

"""


print("-------------- WELCOME TO HILL SCHOOL --------------")
print("ADD STUDENT DETAILS")

studentName = input("Enter Student Name: ")
studentClass = input("Enter Student Class: ")

print("Student details received")

print("ADD STUDENT MARKS")

maths: int = int(input("Maths: "))
english: int = int(input("English: "))
kiswahili: int = int(input("Kiswahili: "))
science: int = int(input("Science: "))
sst: int = int(input("SST: "))

# print(maths,english,kiswahili,science,sst)

totalMarks: int = maths + english + kiswahili + science + sst
averageScore: int = totalMarks/5
grade = "" # Initial Grade

# print(f"Total Marks: {totalMarks}")
# print(f"Average Score: {averageScore}")



if 100 > averageScore >= 80:
    grade = "A"
elif 79 >= averageScore >= 75:
    grade = "A-"
elif 74 >= averageScore >= 70:
    grade = "B+"
elif 69 >= averageScore >= 65:
    grade = "B"
elif 64 >= averageScore >= 60:
    grade = "B-"
elif 59 >= averageScore >= 55:
    grade = "C+"
elif 54 >= averageScore >= 50:
    grade = "C"
elif 49 >= averageScore >= 45:
    grade = "C-"
elif 44 >= averageScore >= 40:
    grade = "D+"
elif 39 >= averageScore >= 35:
    grade = "D"
elif 34 >= averageScore >= 30:
    grade = "D-"
elif 29 >= averageScore >= 0:
    grade = "E"
else:
    print("Invalid Marks")

print("-------------- RESULTS CARD --------------")
print(f"Name: {studentName}")
print(f"Class: {studentClass}")
print(f"Total Marks: {totalMarks}")
print(f"Average Score: {averageScore}")
print(f"Grade: {grade}")












#python
