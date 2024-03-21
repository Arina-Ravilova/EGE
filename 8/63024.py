cnt = 0

even = '1357'
odd = '2468'

for x1 in even:
    for x2 in odd:
        for x3 in even:
            for x4 in odd:
                for x5 in even:
                    for x6 in odd:
                        for x7 in even:
                            for x8 in odd:
                                for x9 in even:
                                    for x10 in odd:
                                        for x11 in even:
                                            num = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + x11
                                            if (num.count('1') <= 4 and num.count('2') <= 4 and num.count('3') <= 4 and \
                                                    num.count('4') <= 4 and num.count('5') <= 4 and
                                                    num.count('6') <= 4 and num.count('7') <= 4 and num.count('8') <= 4):
                                                cnt += 1

# Умножаем на 2, т.к. можно начать с чётного и нечётного числа.
print(cnt * 2)
