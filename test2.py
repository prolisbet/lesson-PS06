data = [
['100', '200', '300'],
['400', '500', '600']
]

numbers = []

for row in data:
    for text in row:
        number = int(text)
        numbers.append(number)

print(numbers)

data2 = [
[100, 110, 120],
[400, 500, 600],
[150, 130, 140]
]

list2 = []

for row in data2:
    for item in row:
        if item > 190:
            list2.append(item)

print(list2)
