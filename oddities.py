n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
for i in l:
    if abs(i)%2==0:
        print(f'{i} is even')
    else:
        print(f'{i} is odd')