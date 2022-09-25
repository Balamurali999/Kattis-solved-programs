n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
m = []
for i in range(1, l[-1]):
    if i not in l:
        m.append(i)
if len(m) == 0:
    print('good job')
else:
    for i in m:
        print(i)
