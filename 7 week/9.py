x = {}
with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        lol = line.split()
        for item in lol:
            x[item] = x.get(item, -1) + 1

a = max(x.values())
output = [x for x, y in x.items() if y == a]
print(sorted(output)[0])
