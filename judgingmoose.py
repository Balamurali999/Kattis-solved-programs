l, r = list(map(int, input().split()))
if l == r != 0:
    print(f'Even {2*max(l,r)}')
elif l == r == 0:
    print('Not a moose')
elif l != r:
    print(f'Odd {2*max(l,r)}')
