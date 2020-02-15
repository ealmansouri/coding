spam = [1,2,3]
eggs(spam)
print(spam)

>>> print('cats', 'dogs', 'mice', sep=',')
cats,dogs,mice

-------------------------------------------------------

>>> import copy
>>> spam = ['A', 'B', 'C', 'D']
>>> cheese = copy.copy(spam)
>>> cheese[1] = 42
>>> spam
['A', 'B', 'C', 'D']
>>> cheese
['A', 42, 'C', 'D']

-------------------------------------------------------

>>> supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
>>> for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flame-throwers
Index 3 in supplies is: binders Using range(len(supplies)) in the previously shown for loop is handy because the code in the loop can access the index (as the variable i) and



spam = ['apples', 'bananas', 'tofu', 'cats']

a = len(spam)
b = a - 1
print('spam[0:b] ' + ' and ' )






