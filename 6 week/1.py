def merge(a, b):
    return sorted(a + b)

lol = list(map(int, input().split()))
lol1 = list(map(int, input().split()))

print(*merge(lol, lol1))
