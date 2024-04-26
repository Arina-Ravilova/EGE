line = open('58328.txt').readline()
max_seq = 0
count = 1
for i in range(len(line) - 1):
    if line[i] != line[i + 1]:
        count += 1
    else:
        max_seq = max(max_seq, count)
        count = 1
print(max_seq)

# Альтернативное решение
for i in range(10):
    # Cлучай с повторяющимися более двух раз цифрами
    # replace заменят два символа и следующая проверка начинается со следующего символа
    # '111'.replace('11', '1 1') => '1 11'
    while f'{i}{i}' in line:
        line = line.replace(f'{i}{i}', f'{i} {i}')
parts = line.split()
# key - функция, которая используется для сравнения каждого элемента списка
print(len(max(parts, key=len)))