n = int(input())
for i in range(n):
    l = list(map(float, input().split()))
    b = int(l[0])
    p = l[1]
    v = 60/p
    a = v*b
    print('{:.4f}'.format(a-v), '{:.4f}'.format(a), '{:.4f}'.format(a+v))
