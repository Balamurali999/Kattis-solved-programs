n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
m = []
for i in l:
    a = i%10
    i = i//10
    m.append(i**a)
print(sum(m))
