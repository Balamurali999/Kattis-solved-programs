l = list(map(int, input().split()))
while l != [1, 2, 3, 4, 5]:
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            t = l[i]
            l[i] = l[i+1]
            l[i+1] = t
            print(*l)
