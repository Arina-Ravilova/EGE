def f(n):
    if n == 0:
        return 0
    return f(n // 10) + (n % 10)


count = 0
for i in range(765432019, 1542613239 + 1, 10):
    count += 1
print(count)
