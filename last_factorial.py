n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

a = []
for j in l:
    f = 1
    for i in range(j, 1, -1):
        f *= i
    a.append(f)
c = []
for i in a:
    b = []
    for j in str(i):
        b.append(j)
    c.append(b[-1])

for i in range(len(c)):
    print(c[i])
