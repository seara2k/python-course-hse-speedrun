n = int(input())
lol = []
for i in range(n):
    line = input().split()
    line[1] = int(line[1])
    lol.append(line)

lol.sort(key=lambda x: x[1], reverse=True)
for item in lol:
    print(item[0])
