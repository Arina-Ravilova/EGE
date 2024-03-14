from itertools import product

cnt = 0
for i in product('012345678', repeat=11):
    if i.count('0') == 0 and i.count('1') <= 4 and i.count('2') <= 4 and i.count('3') <= 4 and i.count('4') <= 4 and i.count('5') <= 4 and i.count('6') <= 4 and i.count('7') <= 4 and i.count('8') <= 4:
        for u in i:
            if (i[u] % 2 ==0 and i[u+1] % 2 !=0) or (i[u+1] % 2 ==0 and i[u] % 2 !=0):
                cnt += 1
print(cnt)
