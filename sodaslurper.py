e, f, r = list(map(int, input().split()))
eb = e+f
t = 0
while r <= eb:
    l = eb % r
    n = eb//r
    t += n
    eb = l+n
print(t)
