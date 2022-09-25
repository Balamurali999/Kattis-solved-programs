l = list(input())
m = ['']
[m.append(x) for x in l if x != m[-1]]
print(''.join(m))
