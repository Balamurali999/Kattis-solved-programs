import math
r, c = list(map(int, input().split()))
r1 = r - c
a = (math.pi)*((2*r)**2)
a1 = (math.pi)*((2*r1)**2)
a = (a1/a)*100
print("{:.6f}".format(a))
