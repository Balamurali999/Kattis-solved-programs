n = int(input())
l=[]
for i in range(n):
    l.append(input())
m = []
for i in range(len(l)):
    if i % 2 == 0:
        m.append(l[i])
for i in range(len(m)):
    print(m[i], end=' ')
