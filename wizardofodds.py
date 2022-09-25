import math
n, k = list(map(int, input().split()))
print('Your wish is granted!') if math.log2(n) <= (k) else print('You will become a flying monkey!')