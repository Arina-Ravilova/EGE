a = [0] * 1000000
for i in range(1, 100000):
    b = bin(i)[2:]
    s = b + (bin(i % 4)[2:])
    R = int(s, 2)
    a[R] = 1
res = 0
for i in range(100000):
    res = max(res, sum(a[i:i + 49]))
print(res)

# сама написала алгоритм по получению нового числа
# а вот метод перебора подсмотрела
