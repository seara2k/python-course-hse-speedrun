lol = []
while True:
    a = int(input())
    if a == 0:
        break
    lol.append(a)
lol.remove(max(lol))
print(max(lol))
