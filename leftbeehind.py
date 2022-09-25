while True:
    a,b=list(map(int,input().split()))
    if a == 0 and b == 0:
        break
    if a + b == 13:
        print('Never speak again.')
    elif a<b:
        print('Left beehind.')
    elif a==b:
        print('Undecided.')
    else:
        print('To the convention.')

