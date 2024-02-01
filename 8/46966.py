from itertools import permutations, product

gs = product('АО', repeat=2)
sgl = permutations('РСМХ', 2)
nope = []
for g in gs:
    glas = ''.join(g)
    nope.append(glas)
for s in sgl:
    soglas = ''.join(s)
    nope.append(soglas)

words = set()
items = permutations('РОСОМАХА')
for item in items:
    line = ''.join(item)
    flag = True
    for no in nope:
        if line.count(no) != 0:
            flag = False
    if flag:
        words.add(line)
print(len(words))
