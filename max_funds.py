n = int(input())
l = list(map(int, input().split()))
k = int(input())
m = []
for i in range(k):
    m.append(list(map(int, input().split())))
print(sum(l))
