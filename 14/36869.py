def conv9(n):
    res = []
    while n > 0:
        res.append(n%9)
        n = n//9
    return res

x = 729**8-3**18+85
x = str(conv9(x))
print(x.count('0'))