l = list(map(int, input().split()))
m = list(map(int, input().split()))
h = l[0]
w = l[1]
n = l[2]
c = 0
for i in range(len(m)):
    c = c+m[i]
    if c == (h*w):
        print('YES')
        break
    elif c > (h*w):
        print('NO')
        break
