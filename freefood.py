n = int(input())
l=[]
for i in range(n):
    x=input().split()
    a=int(x[0])
    b=int(x[1])
    for j in range(a,b+1):
        l.append(j)
print(len(set(l)))