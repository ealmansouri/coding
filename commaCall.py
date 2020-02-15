
def commaCall(usersList):
    a = len(usersList)
    b = a - 1
    firstList = (usersList[0:b])
    endList = usersList[-1]
    print(", ".join(firstList) + ' and ' + str(endList))
    
usersList = []

while True:
    print('Enter list item ' + str(len(usersList) + 1) + ' (or enter nothing to stop)')
    item = input()
    if item == '':
        break
    usersList += [item]
    
commaCall(usersList)
