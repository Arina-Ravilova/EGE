from itertools import product

cnt = 0
for i in product('012345678', repeat=6):
    if i[0] != '0' and i.count('4') == 1 and i.count('1') + i.count('3') + i.count('5') + i.count('7') == 2:
        cnt += 1
print(cnt)
