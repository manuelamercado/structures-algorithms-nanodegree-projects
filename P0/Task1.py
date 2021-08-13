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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
numbers_texts_sending = [record[0] for record in texts]
numbers_texts_receiving = [record[1] for record in texts]
numbers_calls_calling = [record[0] for record in calls]
numbers_calls_receiving = [record[1] for record in calls]
total = numbers_texts_sending + numbers_texts_receiving + numbers_calls_calling + numbers_calls_receiving
total_unique = set(total)
print(f'There are {len(total_unique)} different telephone numbers in the records.')
