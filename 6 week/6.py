def CountSort(a):
    c = [0 for i in range(max(a) + 1)]
    for i in range(len(a)):
        c[a[i]] = c[a[i]] + 1
    b = 0
    for j in range(len(c)):
        for i in range(c[j]):
            a[b] = j
            b = b + 1


lol = list(map(int, input().split()))
CountSort(lol)
print(*lol)
