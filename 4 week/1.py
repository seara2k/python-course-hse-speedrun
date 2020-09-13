def min4(*args):
    min_ = args[0]
    for item in args:
        if item < min_:
            min_ = item

    return min_

a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(min4(a, b, c, d))
