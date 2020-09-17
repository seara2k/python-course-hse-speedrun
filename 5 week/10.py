temp = input()
lol = list(map(int, input().split()))
result = int(input())
print(min(lol, key=lambda x: abs(x - result)))
