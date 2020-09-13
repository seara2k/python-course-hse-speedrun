a = input()
first = a.find("f")
second = a.rfind("f")
lol = [first, second]

if -1 in lol:
    if lol[0] == -1:
        if lol[1] != -1:
            print(lol[1])

    if lol[1] == -1:
        if lol[0] != -1:
            print(lol[0])
else:
    print(*set(lol))
