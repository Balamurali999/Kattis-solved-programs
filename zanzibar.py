n = int(input())
x = []
for i in range(n):
    l = list(map(int, input().split()))
    x.append(l)
for l in x:
    a = 0
    for i in range(len(l)-1,0,-1):
        a = abs(a - l[i])
    print(a-2) if a>1 else print(0)
