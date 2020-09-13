def MinDivisor(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return n

n = int(input())

print("YES" if n == MinDivisor(n) else "NO")
