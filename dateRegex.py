#! python3

import re

dateRegex=re.compile('(\d/\d\d/\d\d\d\d)?|(\d\d-\d\d-\d\d\d\d)?|(\d\d\d\d/\d\d/\d\d)?')

#mo2=dateRegex.search('3/14/2015, 03-14-2015, and 2015/3/14')


text=('3/14/2015, 03-14-2015, and 2015/3/14')
matches=[]
for groups in dateRegex.findall(text):
    matches.append(groups[0])
    
if len(matches) > 0:
    print('\n'.join(matches))
else:
    print('No dates found.')