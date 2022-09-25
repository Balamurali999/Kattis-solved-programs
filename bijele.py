a = [1, 1, 2, 2, 2, 8]
l = list(map(int, input().split()))
m = []
for i in range(len(a)):
    m.append(a[i]-l[i])
print(*m)
