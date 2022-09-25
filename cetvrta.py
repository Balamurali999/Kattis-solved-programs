a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
m = [a[0], b[0], c[0]]
n = [a[1], b[1], c[1]]
for i in m:
    if m.count(i)==1:
        print(i,end=' ')
for i in n:
    if n.count(i)==1:
        print(i,end=' ')
