n = int(input())
l = []
for i in range(n):
    a, b = list(map(int, input().split()))
    l.append(b)
x = []
y = []
z = []
for i in l:
    s = 0
    for j in range(1, i+1):
        s += j
    x.append(s)
    s = 0
    for j in range(1, i*2, 2):
        s += j
    y.append(s)
    s = 0
    for j in range(2, (i*2)+2, 2):
        s += j
    z.append(s)
for i in range(n):
    print(f'{i+1} {x[i]} {y[i]} {z[i]}')
