def f(x, y, a, b):
    if x > y:
        return 0
    if x == y:
        return 1
    if a>2:
        a=0
        b=0
        return f(x*2, y, a, b+1)
    elif b>2:
        a = 0
        b = 0
        return f(x+1, y, a+1, b)
    else:
        return f(x+1, y, a+1, b) + f(x*2, y, a, b+1)
a = 0 #сложение
b = 0 #умножение
print(f(1, 14, a, b))