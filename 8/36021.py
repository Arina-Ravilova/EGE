from itertools import product

items = product('ВИШНЯ', repeat=6)
count = 0
for item in items:
    line = ''.join(item)
    if line.count('В') <= 1 and line[0] != 'Ш' and line[-1] not in 'ЯИ':
        count += 1
print(count)