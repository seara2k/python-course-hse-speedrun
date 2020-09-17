x = {}
with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        lol = line.split()
        for item in lol:
            x[item] = x.get(item, -1) + 1


lol = [(y, x) for x, y in x.items()]
lol.sort(key=lambda x: (-x[0], x[1]))
for item in lol:
    print(item[1])
