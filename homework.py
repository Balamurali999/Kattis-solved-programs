n = list(map(str, input().split(';')))
m = []
c = len(n)
for i in n:
    if i.count('-') == 1:
        i = list(map(int, i.split('-')))
        a = (int(i[-1])-int(i[0]))
        c += a
print(c)
