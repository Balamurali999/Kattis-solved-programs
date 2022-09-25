n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
if (n % 2) == 1:
    print('still running')
else:
    odd = []
    even = []
    for i in range(len(l)):
        if (i % 2) == 0:
            odd.append(l[i])
        else:
            even.append(l[i])
    diff = []
    for i in range(len(odd)):
        diff.append((odd[i]-even[i]))
    print(abs(sum(diff)))