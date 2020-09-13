a = input()

output = a.find("f")
if output == -1:
    print("-2")
else:
    output2 = a[output + 1:].find("f")
    if output2 == -1:
        print("-1")

    else:
        print(output2 + len(a) - len(a[output + 1:]))
