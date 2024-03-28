def divs_count(num):
    divs = set()
    for div in range(2, int(num ** 0.5) + 1):
        if num % div == 0:
            divs.add(div)
            divs.add(num // div)
    return sorted(divs)


for num in range(200_000_001, 200_000_050):
    divs = divs_count(num)
    if len(divs) > 5:
        p = divs[0] * divs[1] * divs[2] * divs[3] * divs[4]
        if p < num:
            print(p)
