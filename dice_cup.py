a, b = input().split()
a, b = int(a), int(b)
c = abs(a-b) + 1
d = min(a, b)
for i in range(c):
    d += 1
    print(d)
