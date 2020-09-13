def lol(a):
    x = int(input())
    if x == 0:
        print(a)
    else:
        return lol(x + a)

lol(0)
