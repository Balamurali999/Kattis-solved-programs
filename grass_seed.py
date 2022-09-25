c = float(input())
l = int(input())
q = []
for i in range(l):
    a = list(map(float, input().split()))
    p = a[0]*a[1]
    q.append(p)
print('{:.7f}'.format(sum(q)*c))
