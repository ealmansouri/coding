while True:
    print('What is your name?')
    name = input()
    if name != 'Ezzie':
        continue
    print('Hello Ezzie, what is the password?')
    password = input()
    if password == 'fish':
        break
        print('Access granted.')