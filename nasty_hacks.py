l = []
m = []
for i in range(eval(input())):
    l.append(list(map(int, input().split())))
for i in l:
    r, e, c = i
    # if r > e > c:
    if c+r == e:
        m.append('does not matter')
    elif r+c < e:
        m.append('advertise')
    else:
        m.append('do not advertise')
for i in m:
    print(i)
