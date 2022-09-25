n = int(input())
t = []
d = []
for i in range(n):
    a, b = list(map(int, input().split()))
    t.append(a)
    d.append(b)
s = []
for i in range(1, n):
    s.append((d[i] - d[i-1])//(t[i] - t[i-1]))
print(int(max(s)))
