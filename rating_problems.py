mx = 3
mn = -3
n, k = list(map(int, input().split()))
b = 0
for _ in range(k):
    a = int(input())
    b += a
uj = n - k
mnr = (b + mn*uj)/n
mxr = (b + mx*uj)/n
print(mnr, mxr)
