import re, pyperclip

phone_regex = re.compile(r'''
                        (\d{3}|\d{2})       #First digits
                        (\s|-)?            #Seperator
                        (\d{7})             #Main number
                        ''', re.VERBOSE)

email_regex = re.compile(r'''
                        ([a-zA-Z0-9]+)      #Username
                        (@)                 #Seperator @
                        ([a-zA-Z0-9.-]+)    #Domain name
                        (\.[a-zA-Z]{2,4})   #Suffix
                        ''', re.VERBOSE)

test = 'Hello. my name is guy. My phone number is: 054-7941734 and my email address is: shaguy3@gmail.com'
phone_number = phone_regex.search(test)
email_address = email_regex.search(test)
print('Phone number found:', phone_number.group() + '. Email address found:', email_address.group() + '.')

# TODO: Find matches in clipboard.

# TODO: Copy results to the clipboard.
