n = int(input())

output = set([i for i in range(1, n + 1)])
while True:
    lol_test = input()
    if lol_test == "HELP":
        break
    lol = list(map(int, lol_test.split()))
    ans = input()
    if ans == "YES":
        output &= set(lol)
    elif ans == "NO":
        output -= set(lol)

print(*sorted(list(output)))
