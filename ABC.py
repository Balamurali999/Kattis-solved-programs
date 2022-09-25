l = ['A','B','C']
m = list(map(int, input().split()))
m.sort()
res = dict(zip(l, m))

n = str(input())
o = []
for i in n:
    o.append(i)
for j in o:
    print(res.get(j), end=' ')
