l = []
a = 'Skru op!'
b = 'Skru ned!'
for i in range(int(input())):
    l.append(str(input()))
v = 7
for i in l:
    if i == a and v < 10:
        v += 1
    elif i == b and v >= 0:
        v -= 1
print(v)
