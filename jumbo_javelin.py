n = int(input())
l = []
for i in range(n):
    a = int(input())
    l.append(a)
b = n-1
s = sum(l)
print(s-b)
