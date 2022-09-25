n = int(input())
a = []
fs = 0
f=2
while(f*f<=n):
    if (n%f==0):
        n=n/f
        a.append(f)
        fs=fs+1
    else:
        f=f+1
print(fs+1)