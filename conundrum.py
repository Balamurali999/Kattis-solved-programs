x = str(input())
n = len(x)//3
y = 'PER'*n
c = 0
for i, j in zip(x, y):
    if i != j:
        c += 1
print(c)
