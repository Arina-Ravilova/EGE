count = 0
for i in range(128):
    for j in range(256):
        ip = f'112.208.{i}.{j}'
        bin_ip = ' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')])
        if bin_ip.count('1') % 11 == 0:
            count += 1
print(count)