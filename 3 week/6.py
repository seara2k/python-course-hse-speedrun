p = int(input())
x = int(input())
y = int(input())

x = x * (100 + p)
y = y * (100 + p)

rub = x // 100 + (y + (x % 100) * 100) // 10000
cop = (x % 100 + y // 100) % 100


print(rub, cop)
