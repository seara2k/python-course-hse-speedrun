n = int(input())
stown = list(map(int, input().split()[:n]))
m = int(input())
sbomb = list(map(int, input().split()[:m]))
listTown = []
listBomb = []
j = 1
for i in stown:
    listTown.append((i, j))
    j += 1
j = 1
for i in sbomb:
    listBomb.append((i, j))
    j += 1
listTown.sort()
listBomb.sort()
p = []
k = 0
d = 0
for a in range(n):
    minn = abs(listTown[a][0] - listBomb[d][0])
    while d <= m - 1:
        if abs(listTown[a][0] - listBomb[d][0]) < minn:
            minn = abs(listTown[a][0] - listBomb[d][0])
            k = d
        if d + 1 < m and abs(listTown[a][0] - listBomb[d + 1][0]) > minn:
            d = m + 1
        d += 1
    d = k
    p.append((listTown[a][1], listBomb[k][1]))
p.sort()
p = [p[i][1] for i in range(n)]
print(*p)
