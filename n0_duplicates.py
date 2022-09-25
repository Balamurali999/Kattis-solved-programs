n = list(map(str, input().split()))
f = 0
for i in n:
    if n.count(i) != 1:
        f = 1
        break
if f == 1:
    print('no')
else:
    print('yes')
