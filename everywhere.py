n = int(input())
o = []
for i in range(n):
    t = int(input())
    lst = []
    for j in range(t):
        lst.append(str(input()))
    lst = list(set(lst))
    o.append(len(lst))
for i in o:
    print(i)