s, n = [int(x) for x in input().split()]
lst = []
x = 0
for i in range(n):
    ele = int(input())

    lst.append(ele)
lst.sort()
lol = []
i = 0
while sum(lol) <= s and i <= len(lst) - 1:
    lol.append(lst[i])
    i += 1
    if sum(lol) > s:
        i -= 1
print(i)
