from itertools import permutations

table = '13 14 16 23 24 27 28 31 32 34 38 41 42 43 46 56 57 58 61 64 65 67 72 75 76 78 82 83 85 87'
graph = 'АБ АВ АГ АЖ БВ БД БИ БА ИЕ ИД ИЖ ИБ ЖИ ЖЕ ЖГ ЖА ГА ГЕ ГЖ ВА ВД ВБ ДБ ДВ ДЕ ДИ ЕД ЕГ ЕЖ ЕИ'

print('1 2 3 4 5 6 7 8')
for p in permutations('АБВГДЕЖИ'):
    new_graph = table
    for i in range(1, 9):
        new_graph = new_graph.replace(str(i), p[i - 1])
    # set() - множество, в котором не могут находиться повторяющиеся элементы
    if set(new_graph.split()) == set(graph.split()):
        # 'символ_соединения'.join(список_значений_которые_соединяем)
        print(' '.join(p))
