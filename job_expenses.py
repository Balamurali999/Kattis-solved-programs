n = int(input())
l = list(map(int, input().split()))
m = []
[m.append(i) for i in l if i < 0]
print(sum(m)*-1)
