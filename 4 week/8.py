def power(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    return power(a**2, n / 2) if n % 2 == 0 else a * power(a, n - 1)

a, n = float(input()), int(input())
print(power(a, n))
