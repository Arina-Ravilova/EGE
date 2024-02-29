for a in range(300):
    f = True
    for x in range(300):
        for y in range(300):
            if not ((x + 2 * y < a) or (y > x) or (x > 60)):
                f = False
    if f:
        print(a)
        break
