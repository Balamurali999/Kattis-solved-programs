n=int(input())
for i in range(n):
    a=int(input())
    b=list(map(int,input().split()))
    c=max(b)
    d=min(b)
    e=2*(c-d)
    print(e)