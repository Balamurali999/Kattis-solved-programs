n = int(input())
l = []
for i in range(n):
    a = list(input().split())
    a[1] = int(a[1])
    l.append(a)
m = l
for i in range(len(l)):
    for j in range(len(l)):
        if m[i][2] == l[j][2] and m[i][1] > l[j][1]:
            m[j] = [0, 0, 0]
        elif m[i][2] == l[j][2] and m[i][1] < l[j][1]:
            m[i] = [0, 0, 0]

x = []
for i in m:
    if i != [0, 0, 0]:
        x.append(i)
x.sort()
print(len(x))
for i in range(len(x)):
    print(x[i][0])
