def conv9(n):
    conv_str = ''
    while n > 0:
        conv_str = str(n % 9) + conv_str
        n //= 9
    return conv_str

cnt = 0
for i in range(100000, 1000000):
    i = conv9(i)
    if i.count('4') == 1 and i.count('1')+i.count('3')+i.count('5')+i.count('7') == 2:
        cnt += 1
print(cnt)