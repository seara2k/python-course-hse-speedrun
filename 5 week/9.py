lol1 = list(map(int, input().split()))
prev = lol1[0]
for i in range(len(lol1)):
    if lol1[i] > prev:
        print(lol1[i], end=" ")
    prev = lol1[i]
