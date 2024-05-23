def game(heap, moves, to):
    if heap >= 435:
        return moves % 2 == to % 2
    if moves == to:
        return False
    h = [game(heap + 5, moves + 1, to), game(heap * 3, moves + 1, to)]
    # Если бы в задаче было написано, что известно, что кто-то выиграл каким-то ходом, то
    # в return указывается просто any(h)
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)


print(f'19: {min(s for s in range(1, 434) if not game(s, 0, 1) and game(s, 0, 2))}')
print(f'20: {[s for s in range(1, 434) if not game(s, 0, 1) and game(s, 0, 3)]}')
print(f'21: {min(s for s in range(1, 434) if not game(s, 0, 2) and game(s, 0, 4))}')