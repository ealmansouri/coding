# This program says hello and asks for my name

print('Hello World!')
print('What is your name?')
myName = input()

print('It is good to meet you ' + myName)
nameLength = str(len(myName))

print('The length of your name is ' + nameLength + ' characters long') 
print('What is your age?')
myAge = input()
print('Your will be ' +str(int(myAge) + 1) + ' next year.')
