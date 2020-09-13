def summ(a, b):
    if b == 0:
        return a
    if a == 0:
        return b
    return summ(a + 1, b - 1)

a, b = int(input()), int(input())
print(summ(a, b))
