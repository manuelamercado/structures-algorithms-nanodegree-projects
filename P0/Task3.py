"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def isMobile(number):
    if number.startswith('7'):
        return True
    elif number.startswith('8'):
        return True
    elif number.startswith('9'):
        return True
    False


calls_from_bangalore_codes = []
calls_from_bangalore_to_numbers = []

for record in calls:
    if record[0].startswith('(080)'):
        calls_from_bangalore_to_numbers.append(record[1])

        if record[1].startswith('('):
            match = re.match('\(.+\)', record[1])
            code = match[0].replace('(', '').replace(')', '')
            calls_from_bangalore_codes.append(code)
        elif (' ' in record[1]) and isMobile(record[1]):
            match = record[1].split(' ')
            code = match[0][0:4]
            calls_from_bangalore_codes.append(code)
        elif record[1].startswith('140'):
            calls_from_bangalore_codes.append('140')

calls_from_bangalore_codes_unique = set(calls_from_bangalore_codes)
calls_from_bangalore_codes = sorted(calls_from_bangalore_codes_unique)
print('The numbers called by people in Bangalore have codes:')
for code in calls_from_bangalore_codes:
    print(code)

total_calls_from_bangalore = len(calls_from_bangalore_to_numbers)
total_calls_to_bangalore = 0
for number in calls_from_bangalore_to_numbers:
    if number.startswith('(080)'):
        total_calls_to_bangalore += 1

percentage = (total_calls_to_bangalore / total_calls_from_bangalore) * 100.00
print(f'{round(percentage, 2)} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')
