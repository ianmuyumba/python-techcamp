# LIMIT LOGIN ATTEMPTS



print("Enter Username and Password. You only have three attempts")

userName = "ian"
password = 0000

attempts = 3

while attempts > 0:
	login_username = input("Username: ")
	login_password = int(input("Password: "))

	if login_username == userName and login_password == password:
		print("Login Succesful")
		break
	else:
		print(f"Login Failed. You have {attempts-1} attempts left")
		attempts -= 1










































	#Python