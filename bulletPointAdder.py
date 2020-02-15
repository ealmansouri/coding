#! python3
# bulletPointAdder.py Adds Wikipedia bullet points to the start
# of each line of text in the clipboard.

import pyperclip
text = pyperclip.paste()

# TODO: Seperate lines and add stars.

lines = text.split('\n')
for i in range(len(lines)):	#loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add a star to each string in "lines" list

text = '\n'.join(lines)
pyperclip.copy(text)
