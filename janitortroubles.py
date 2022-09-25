import math
n = list(map(int, input().split()))
a, b, c, d = n
s = sum(n)/2
ans = math.sqrt((s-a)*(s-b)*(s-c)*(s-d))
print('{:.6f}'.format(ans))
