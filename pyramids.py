n = int(input())
a=[]
for i in range(10000):
    if i % 2 == 1:
        a.append(i*i)
s = 0
c = 0
for i in range(len(a)):
    s = s + a[i]
    if s > n:
        break
    elif s == n:
        c = c+1
    else:
        c = c+1
print(c)