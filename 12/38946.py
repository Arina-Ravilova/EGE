def convert(s):
    while '111' in s or '222' in s:
        s = s.replace('111', '22', 1)
        s = s.replace('222', '1', 1)
    return s


for i in range(201, 400):
    s = '1' * i
    if '2' not in convert(s):
        print(i)
        break
