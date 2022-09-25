while True:
    n = int(input())
    if n == (-1):
        break
    l = []
    for i in range(n):
        a = list(map(int, input().split()))
        l.append(a)
    for x in range(len(l)-1, 0, -1):
        l[x][1] -= l[x-1][1]
    s = 0
    for x in l:
        s += (x[0]*x[1])
    print(f'{s} miles')