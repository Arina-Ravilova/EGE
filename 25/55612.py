from fnmatch import fnmatch

for x in range(3013, 10**10 + 1, 3013):
    if fnmatch(str(x), '1?3948*5'):
        print(x)
