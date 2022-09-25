n = str(input())
a = []
b = []

for j in n:
    a.append(j)

for i in range(len(a)):
    if a[i] == ':' and (i<=(len(a)-2)):
        if a[i + 1] == '-':
            if a[i + 2] == ')':
                b.append(i)
        elif a[i + 1] == ')':
            b.append(i)
    elif a[i] == ';':
        if a[i + 1] == '-':
            if a[i + 2] == ')':
                b.append(i)
        elif a[i + 1] == ')':
            b.append(i)

for k in range(len(b)):
    print(b[k])
