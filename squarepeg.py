import math
a, b = list(map(int, input().split()))
c = b*math.sqrt(2)
print('fits') if c > a else print('nope')
