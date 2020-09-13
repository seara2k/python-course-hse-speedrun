def lol():
    x = int(input())
    if x == 0:
        print("0")
        return
    lol()
    print(x)

lol()
