while True:
	print('Enter your age:')
	age=input()
	if age.isdecimal():
		break
	print('Please enter an integer for your age')
	
while True:
    print('Please type a password:')
    password=input()
    if password.isalnum():
        break
    print('Password must contain only letters and integers')