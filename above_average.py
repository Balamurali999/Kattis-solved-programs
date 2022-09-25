n = int(input())
m = []
for i in range(n):
    l = list(map(int, input().split()))
    m.append(l)
for j in m:
    a = sum(j[1:])
    b = (j[0])
    d = (a / b)
    c = 0
    for q in j[1:]:
        if q > d:
            c = c+1
    p = (c/b)*100
    print('{:.3f}%'.format(p))
    