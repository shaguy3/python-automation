import re
import os

american_regex = re.compile(r'''
                            (0?[1-9]|1[0-2])                #Day
                            (/|.|-)                         #First Seperator
                            (0?[1-9]|1[0-9]|2[0-9]|30|31)   #Month
                            (/|.|-)                         #Second seperator
                            (\d{4}|\d{2})                   #Year)
                            ''', re.VERBOSE)

test_date = '02.15/19'

mo = american_regex.search(test_date)

print('Date found: ' + mo.group())
