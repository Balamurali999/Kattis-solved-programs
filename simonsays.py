n = int(input())
for i in range(n):
    a = input()
    if 'Simon says' in a:
        print(a[11:])
