a = input()
first = a.find("h")
second = a.rfind("h")

lol = a[first:second + 1]
print(a.replace(lol, ""))
