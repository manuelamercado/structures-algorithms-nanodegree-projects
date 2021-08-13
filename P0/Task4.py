"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
calling_numbers = []
receiving_numbers = []
msg_numbers = []

for record in calls:
    calling_numbers.append(record[0])
    receiving_numbers.append(record[1])

for record in texts:
    msg_numbers.append(record[0])
    msg_numbers.append(record[1])

calling_numbers = set(calling_numbers)
receiving_numbers = set(receiving_numbers)
calling_numbers = calling_numbers - receiving_numbers

msg_numbers = set(msg_numbers)
calling_numbers = calling_numbers - msg_numbers

calling = sorted(calling_numbers)
print('These numbers could be telemarketers:')
for number in calling:
    print(number)
