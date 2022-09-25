n = int(input())
l = []
for i in range(n):
    a, b = list(map(int, input().split()))
    l.append(b-a)
s = sum(l)
print(s/n)
