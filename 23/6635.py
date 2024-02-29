# Ограничение "содержится ровно 13 команд"
s = set()


def f(x, step):
    if step == 13:
        if x < 0:
            s.add(x)
    else:
        f(x - 3, step + 1)
        f(x * -3, step + 1)


f(333, 0)
print(len(s))
