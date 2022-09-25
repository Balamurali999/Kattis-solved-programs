n = int(input())
for i in range(n):
    l = input()
    if l == 'P=NP':
        print('skipped')
    else:
        a, c = list(map(int, l.split('+')))
        print(a+c)
