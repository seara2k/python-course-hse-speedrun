a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*[x for x in a if x in b])
