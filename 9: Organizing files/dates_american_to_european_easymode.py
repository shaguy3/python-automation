import re
import os

test = 'bdhiscbhdsicbiu 04/10/2013 cjicbxyuogyzo 02/15/18'

american_regex = re.compile(r'''
                            (.*?)                           #Before
                            (0?[1-9]|1[0-2])                #Month
                            (/)                             #Separator 1
                            (0?[1-9]|1[0-9]|2[0-9]|30|31)   #Day
                            (/)                             #Separator 2
                            (\d{2,4})                       #Year
                            (.*)                            #After
                            ''', re.VERBOSE | re.DOTALL)

for mo in american_regex.findall(test):
    if mo is None:
        print('date not found')
    else:
        print(test)
        print(mo)
        before, month, separator1, day, separator2, year, after = mo
        print(before + day + separator1 + month + separator2 + year + after)
