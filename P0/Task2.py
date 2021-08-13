"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

max_time_calling = 0
max_number_on_phone = ''
calls_duration_numbers = {}

for record in calls:
    calls_duration_numbers[record[0]] = calls_duration_numbers.get(record[0], 0) + int(record[3])
    calls_duration_numbers[record[1]] = calls_duration_numbers.get(record[1], 0) + int(record[3])

max_number_on_phone = max(
    calls_duration_numbers,
    key=lambda k:calls_duration_numbers[k]
)
max_time_calling = calls_duration_numbers[max_number_on_phone]

print(f'{max_number_on_phone} spent the longest time, {max_time_calling} seconds, on the phone during September 2016.')