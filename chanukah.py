n = int(input())
x = []
y = []
for i in range(n):
    x.append(list(map(int, input().split())))
for i in x:
    a = i[1]
    t = 1
    s = 0
    for j in range(a):
        s += t
        t += 1
    y.append(s+a)
for i in range(len(y)):
    print(i+1, y[i])
