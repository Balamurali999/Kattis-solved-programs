l = []
n = int(input())
for i in range(n):
    l.append(int(input()))
l.sort()
l = l[::-1]
m = []
for i in range((n//3)+1):
    m.append(l[(i*3):(i*3)+3])
for i in range(len(m)):
    if len(m[i]) == 3:
        m[i] = m[i][:-1]
k = []
for i in m:
    k.extend(i)
print(sum(k))
