import re
import os


def swap_date(string, regex):
    match_object = regex.search(string)
    if match_object is None:
        return string
    else:
        if match_object.group(4) == '/':
            before, month, blank1, separator1, day, separator2, blank2, blank3, blank4, blank5, blank6, blank7, year, \
                after = match_object.groups()
        elif match_object.group(7) == '.':
            before, month, blank1, blank2, blank3, blank4, separator1, day, separator2, blank5, blank6, blank7, year, \
                after = match_object.groups()
        else:
            before, month, blank1, blank2, blank3, blank4, blank5, blank6, blank7, separator1, day, separator2, year, \
                after = match_object.groups()
        return before + day + separator1 + month + separator2 + year + swap_date(after, regex)


american_regex = re.compile(r'''
                            (.*?)
                            (0?[1-9]|1[0-2])                              #Month
                            ((/)(0?[1-9]|1[0-9]|2[0-9]|30|31)(/)
                            |(\.)(0?[1-9]|1[0-9]|2[0-9]|30|31)(\.)
                            |(-)(0?[1-9]|1[0-9]|2[0-9]|30|31)(-))         #Day(with separators)
                            (\d{2,4})                                     #Year
                            (.*)
                            ''', re.VERBOSE | re.DOTALL)

parent_folder = os.getcwd() + '/American Dates'
for folder_name, sub_folders, file_names in os.walk(parent_folder):
    for file_name in file_names:
        current_file = open(folder_name + '/' + file_name, 'r')
        contents = current_file.read()
        after_swap = swap_date(contents, american_regex)
        os.chdir('/home/guy/PycharmProjects/python-automation/9: Organizing files/European dates')
        new_file = open(os.path.splitext(file_name)[0] + '_Euro.txt', 'w')
        new_file.write(swap_date(contents, american_regex))
        new_file.close()
