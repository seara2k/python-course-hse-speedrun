number_of_kids = int(input())
lst = []
for j in range(number_of_kids):
    temp = set()
    for i in range(int(input())):

        temp.add(input())
    lst.append(temp)
output = lst[0].copy()
for item in lst:
    output &= item
print(len(output))
print(*output, sep="\n")
output = lst[0].copy()
for item in lst:
    output |= item
print(len(output))
print(*output, sep="\n")
