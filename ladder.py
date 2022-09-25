import math
l = list(map(int, input().split()))
o, angle = l[0], l[1]
print(math.ceil(o/(math.sin(math.radians(angle)))))
