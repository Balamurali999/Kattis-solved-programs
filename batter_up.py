n = int(input())
l = list(map(int, input().split()))
m=[]
for i in range(len(l)):
    if l[i] >= 0:
        m.append(l[i])
a = sum(m)
b = a/len(m)
print(b)
