import sys


f = sys.stdin.read()

f = f.split()
print(len(set(f)))
