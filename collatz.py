# This is my first program on github


def collatz(number):
	number = int(input())
	if (number % 2) == 0:
		((number) // 2)
		return number
	else:
		((3 * (number)) + 1)
		return number


entry = collatz(number)

while entry != 1:
	print(entry)