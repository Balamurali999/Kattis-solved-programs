n = list(map(str, input().split()))
x = n[0]
y = int(n[1])
if x == 'OCT' and y == 31:
    print('yup')
elif x == 'DEC' and y == 25:
    print('yup')
else:
    print('nope')