lol = list()
a, b = int(input()), int(input())
if a < b:
    for i in range(a, b + 1):
        lol.append(i)
else:
    for i in range(b, a + 1):
        lol.append(i)
    lol.reverse()
print(*lol)
