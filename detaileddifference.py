n = int(input())

for k in range(n):
    x = input()
    y = input()
    z = ''
    for i, j in zip(x, y):
        if i == j:
            z += '.'
        else:
            z += '*'
    print(x, '\n', y, '\n', z, '\n')
