x = list(map(str, input().split()))
l = []
for i in x:
    l.append((i[0]))
a = []
for i in l:
    a.append(l.count(i))
print(max(a))
