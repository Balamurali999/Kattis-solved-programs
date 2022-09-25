n = int(input())
l = []
for i in range(n):
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    l.append(1) if a+b == c or abs(a-b) == c or a*b == c or (a/b == c or b/a == c) else l.append(0)
for i in l:
    print('Possible') if i == 1 else print('Impossible')
