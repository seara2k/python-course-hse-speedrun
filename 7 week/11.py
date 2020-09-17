x = {}
with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        line = line.strip()
        x[line] = x.get(line, 0) + 1

lol = [(y, x) for x, y in x.items()]
lol.sort()
with open('output.txt', 'w', encoding='utf8') as f:
    if lol[-1][0] / sum(x.values()) > 0.5:
        f.write(lol[-1][1])
    else:
        f.write(lol[-1][1])
        f.write("\n")
        f.write(lol[-2][1])
