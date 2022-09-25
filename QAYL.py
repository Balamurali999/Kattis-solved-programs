n = int(input())
l = []
for i in range(n):
    a = list(map(float, input().split()))
    b = a[0]*a[1]
    l.append(b)
s =sum(l)
print("{:.3f}".format(s))
