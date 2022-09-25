l = []
for i in range(3):
    l.append(input())
if l[1] == '+':
    print(int(l[0]) + int(l[2]))
else:
    print(int(l[0]) * int(l[2]))
