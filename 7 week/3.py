lol1 = list(map(int, input().split()))
a = set()
for item in lol1:
    if item in a:
        print("YES")
    else:
        print("NO")
    a.add(item)
