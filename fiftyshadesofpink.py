n = input()
c = 0
for i in range(int(a)):
    b = input().lower()

    if (("rose" in b) or ("pink" in b)):
        c += 1

if (c == 0):
    print("I must watch Star Wars with my daughter")
else:
    print(c)
