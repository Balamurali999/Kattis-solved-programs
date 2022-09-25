j = [0]
for i in range(5):
    m = list(map(int, input().split()))
    j.append(sum(m))
a = max(j)
b = j.index(a)
print(b, a)
