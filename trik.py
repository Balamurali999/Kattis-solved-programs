l = []
a = str(input())
for i in a:
    l.append(i)
x = l[0].upper()
s = [1, 2, 3]
index = 0
for i in x:
    if i == 'A':
        s[0], s[1] = s[1], s[0]
        index = 2
    elif i == 'B':
        s[1], s[2] = s[2], s[1]
        index = 0
    elif i == 'C':
        s[0], s[2] = s[2], s[0]
        index = 1
print(s[index])