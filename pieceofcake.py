a = list(map(int, input().split()))
l = a[0]
h = a[1]
v = a[2]
h1 = max(h, l-h)
v1 = max(v, l-v)
b = h1*v1*4
print(b)
