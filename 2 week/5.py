a = int(input())

if ((10 < a < 20) or ((a % 10) in [0, 5, 6, 7, 8, 9])):
    print(a, "korov")
elif a % 10 == 1:
    print(a, "korova")
else:
    print(a, "korovy")
