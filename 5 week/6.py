lol = input()

lol1 = lol.split()
lol2 = []
lol1 = list(map(int, lol1))
[print(lol1[i], end=" ") for i in range(len(lol1)) if lol1[i] % 2 == 0]
