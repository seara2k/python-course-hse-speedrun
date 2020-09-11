lol = []
while True:
    a = int(input())
    if a == 0:
        break
    if a % 2 == 0:
        lol.append(a)

print(len(lol))
