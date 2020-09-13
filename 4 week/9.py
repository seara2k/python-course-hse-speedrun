import math
n, m = int(input()), int(input())
k = math.gcd(n, m)
print(n // k, m // k)
