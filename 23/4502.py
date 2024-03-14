s = set()

def f(x, step):
    if step == 6:
        if 34 <= x <= 59:
            s.add(x)
    else:
        f(x + 1, step + 1)
        f(x + 2, step + 1)
        f(x * 2, step + 1)

f(1, 0)
print(len(s))