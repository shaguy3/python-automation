import re
import os

american_regex = re.compile(r'''
                            (.*?)
                            (0?[1-9]|1[0-2])                              #Month
                            ((/)(0?[1-9]|1[0-9]|2[0-9]|30|31)(/)
                            |(\.)(0?[1-9]|1[0-9]|2[0-9]|30|31)(\.)
                            |(-)(0?[1-9]|1[0-9]|2[0-9]|30|31)(-))         #Day(with separators)
                            (\d{2,4})                                     #Year
                            (.*)
                            ''', re.VERBOSE | re.DOTALL)

# TODO: Loop over the files in the working directory
parent_folder = os.getcwd() + '/American Dates'
for folder_name, sub_folders, file_names in os.walk(parent_folder):
    for file_name in file_names:
        print('found file: ' + file_name)
        # TODO: skip files without a date
        current_file = open(folder_name + '/' + file_name, 'r')
        contents = current_file.read()
        #print(american_regex.findall(contents))
        if american_regex.search(contents) is not None:
            # TODO: Get the different parts of the filename
            for date in american_regex.findall(contents):
                before = date[0]
                month = date[1]
                separator_1 = date[5]
                day = date[6]
                separator_2 = date[7]
                year = date[11]
                after = date[12]
                print(before + day + separator_1 + month + separator_2 + year + after)
        current_file.close()

    # TODO: Rename the files
