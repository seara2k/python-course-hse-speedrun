
x = []
with open('input.txt', 'r', encoding='utf8') as f:
    k = f.readline()
    k = k.strip()
    for line in f:
        lol = line.split()
        j = 0
        for i in range(-1, -4, -1):

            lol[i] = int(lol[i])
            if lol[i] < 40:
                j = 1
        if j == 0:
            x.append(sum(lol[:-4:-1]))
x.sort()
# print(x)
k = int(k)
if x.count(x[-1]) > k:
    output = 1
elif len(x) <= k:
    output = 0
else:
    i = 0
    while True:
        output = x[-k + i]
        temp = [test for test in x if test >= output]
        if len(temp) <= k:
            break
        i += 1
    # print(output)

with open('output.txt', 'w', encoding='utf8') as f:
    f.write(str(output))
