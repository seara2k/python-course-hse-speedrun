
x = []
with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        lol = line.split()
        x.append(lol)
x.sort(key=lambda x: x[0])
for i in range(len(x)):
    x[i].pop(2)
    x[i] = " ".join(x[i])
with open('output.txt', 'w', encoding='utf8') as f:
    f.writelines(line + '\n' for line in x)
