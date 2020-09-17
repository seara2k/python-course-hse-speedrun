lol1 = list(map(int, input().split()))
max_ = max(lol1)
output = 0
for i in range(len(lol1)):
    if lol1[i] == max_:
        output = i
print(max_, output)
