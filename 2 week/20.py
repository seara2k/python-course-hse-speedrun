lol = []
prev = int(input())
count = 1
while True:
    a = int(input())
    if a == prev:
        count = count + 1
    elif a == 0:
        lol.append(count)
        break
    else:
        lol.append(count)
        count = 1
        prev = a

print(max(lol))
