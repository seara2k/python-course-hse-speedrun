lol = list(map(int, input().split()))
for i in range(0, len(lol), 2):
    try:
        (lol[i], lol[i + 1]) = (lol[i + 1], lol[i])
    except IndexError:
        pass

print(*lol)
