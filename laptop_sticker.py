l = list(map(int, input().split()))
a, b, c, d = l
a -= 2
b -= 2
if a >= c and b >= d:
    print(1)
else:
    print(0)