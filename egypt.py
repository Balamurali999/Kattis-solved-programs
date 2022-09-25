while True:
    l = list(map(int, input().split()))
    l.sort()
    if l == [0]*3:
        break
    a, b, c = l[0], l[1], l[2]
    print('right') if (a**2)+(b**2) == (c**2) else print('wrong')
