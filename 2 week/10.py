a = int(input())
x = 1
lol = []
while True:
    lol.append(x**2)
    x = (x + 1)
    if x**2 > a:
        break
print(*lol)
