s, t, n = list(map(int, input().split()))
w = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

for i in range(n):
    s += w[i]

    waiting = 0 if s % c[i] == 0 else c[i] - s % c[i]
    s += waiting

    s += b[i]
s += w[-1]
print("yes") if s <= t else print("no")



