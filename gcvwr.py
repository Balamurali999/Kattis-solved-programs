a, b, c = list(map(int, input().split()))
s = sum(list(map(int, input().split())))
a = (a-b) * 0.9
print(int(a-s))