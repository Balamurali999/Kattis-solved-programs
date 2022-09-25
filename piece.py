l = list(map(int, input().split()))

a = abs(10 - l[0])
b = 4
c = abs(10 - l[2])

m = max(a, l[0])
o = max(c, l[2])
print(m, o)
print(m*b*o)
