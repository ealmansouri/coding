#! python3

import pyperclip, re


urlsRegex = re.compile(r'''(
(http|https)?
(://)
([w]{3})
(\.[a-zA-Z0-9.-]+)?
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in urlsRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('- URL number ' + str(groups) + '\n'.join(matches))
else:
    print('No URL\'s found')