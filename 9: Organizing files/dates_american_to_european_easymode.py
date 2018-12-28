import re
import os


def swap_date(string, regex):
    match_object = regex.search(string)
    if match_object is None:
        return string
    else:
        before, month, separator1, day, separator2, year, after = match_object.groups()
        return before + day + separator1 + month + separator2 + year + swap_date(after, regex)


test = 'bdhiscbhdsicbiu 04/10/2013 cjicbxyuogyzo02/2/18 cbucbuascbuaso \n cbjkicbiasbcskbjk 03/10/2010'

american_regex = re.compile(r'''
                            (.*?)                           #Before
                            (0?[1-9]|1[0-2])                #Month
                            (/)                             #Separator 1
                            (0?[1-9]|1[0-9]|2[0-9]|30|31)   #Day
                            (/)                             #Separator 2
                            (\d{2,4})                       #Year
                            (.*)                            #After
                            ''', re.VERBOSE | re.DOTALL)

test_after_swap = swap_date(test, american_regex)

print(test)
print(test_after_swap)
