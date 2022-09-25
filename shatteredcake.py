n=int(input())
t=int(input())
c=0
for i in range(t):
    a,b=list(map(int,input().split()))
    c+=a*b
print(int(c/n))