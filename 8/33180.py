from itertools import product

items = product('ТИМОФЕЙ', repeat=5)
count =0
for item in items:
    line=''.join(item)
    if line.count('Й') <= 1 and line[0] != 'Й' and line[-1] != 'Й' and line.count('ЙИ')==0 and line.count('ИЙ')==0:
        count+=1
print(count)