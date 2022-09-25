l = []
for i in range(int(input())):
    l.append(list(input().split()))
for i in range(len(l)):
    l[i] = l[i][0] + l[i][1]
m = []
for i in l:
    if i not in m:
        m.append(i)

