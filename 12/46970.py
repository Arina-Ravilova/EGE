from itertools import product, combinations_with_replacement


def convert(s):
    while '00' not in s:
        s = s.replace('01', '210', 1)
        s = s.replace('02', '3101', 1)
        s = s.replace('03', '2012', 1)
    return s

for i in range(3, 50):
    mid = combinations_with_replacement('123', i)
    for m in mid:
        m = ''.join(m)
        s = '0' + m + '0'
        if convert(s).count('1')==70 and convert(s).count('2')==56 and convert(s).count('3')==23:
            print(i+2)
            break