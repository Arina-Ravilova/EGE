from itertools import permutations, product
gs = product('АО', repeat=2)
sgl = permutations('РСМХ', 2)
nope = []
cnt = 0
for g in gs:
    glas = ''.join(g)
    nope.append(glas)
for s in sgl:
    soglas = ''.join(s)
    nope.append(soglas)

items = permutations('РОСОМАХА', 8)
for item in items:
    line = ''.join(item)
    sm_count = 0
    for no in nope:
        if line.count(no) == 0:
            sm_count += 1
        if sm_count == 16:
            cnt+=1
print(cnt)

