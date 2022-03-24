data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

for a in data_tuple:
    if type(a) == str:
        letters.append(a)
    else:
        numbers.append(a)

del numbers[0]
letters.append(numbers.pop(0))
numbers.insert(1, 2)

numbers.sort()
letters.reverse()
letters[1] = letters[1].upper()
letters[-2] = letters[-2].lower()

numbers = tuple(numbers)
letters = tuple(letters)

print(letters, numbers)
