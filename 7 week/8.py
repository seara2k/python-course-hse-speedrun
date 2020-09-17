n = int(input())
lol = {}
for i in range(n):
    line = input().split()
    lol[line[1]] = line[0]
    lol[line[0]] = line[1]
word = input()
print(lol[word])
