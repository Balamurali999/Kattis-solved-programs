'''n = int(input())
l = list(input().split())
for i in range(n):
    if l[i] == 'mumble':
        l[i] = i+1
c = 1
f = 1
print(l)
for i in l:
    if c == int(i):
        f = 0
    else:
        f = 1
    c += 1
print('makes sense') if f == 0 else print('something is fishy')'''


numberOfBites = int(input())
counts = input().split()
makesSense = True
for biteNumber, count in enumerate(counts, 1):
    if count == "mumble":
        continue
    else:
        count = int(count)
        if count != biteNumber:
            makesSense = False

if makesSense:
    print("makes sense")
else:
    print("something is fishy")