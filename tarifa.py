m = int(input())
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
t = n*m
s = sum(l)
a = (t-s)+m
print(a)