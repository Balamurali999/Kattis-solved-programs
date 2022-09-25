a, b, n = list(map(int, input().split()))
for i in range(n):
    l = list(map(int, input().split()))
    l = l[1:]
    print('KEEP') if (a and b) in l else print('REMOVE')

