myPets = ['Tom','Jerry','Harry','Snowy']
print('Enter a pet name: ')

name=input()
if name not in myPets:
    print('Sorry, I do not have a pet named ' + str(name))
else:
    print(name + ' is my pet')