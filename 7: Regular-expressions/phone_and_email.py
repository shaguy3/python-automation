import re

phone_regex = re.compile(r'''
                        (\d{3}|\d{2})        #First digits
                        (\s|-)?              #Seperator
                        (\d{7})              #Main number
                        ''', re.VERBOSE)

email_regex = re.compile(r'''
                        ([a-zA-Z0-9.]+)      #Username
                        (@)                  #Seperator @
                        ([a-zA-Z0-9.]+)      #Domain name
                        (\.[a-zA-Z.]{2,4})   #Suffix
                        ''', re.VERBOSE)

results_phones = []
results_emails = []

with open('text_source.txt', 'r') as file:
    phones = phone_regex.findall(file.read())
    for phone in phones:
        current_phone = ''
        for group in phone:
            current_phone += group
        results_phones.append(current_phone)
    file.close()
with open('text_source.txt', 'r') as file:
    emails = email_regex.findall(file.read())
    for email in emails:
        current_email = ''
        for group in email:
            current_email += group
        results_emails.append(current_email)
    file.close()


print('Phones found: ' + str(results_phones))
print('emails found: ' + str(results_emails))
