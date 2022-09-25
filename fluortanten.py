'''n = int(input())
l = list(map(int, input().split()))
m = []
for i in range(n):
    a = []
    if i == 0:
        for j in l:
            if j == 0:
                l.remove(0)
                l.insert(0, j)
        for k in range(1, n+1):
            a.append(l[k-1]*k)
        m.append(sum(a))
        print(a)
    elif i == 1:
        for j in l:
            if j == 0:
                l.remove(0)
                l.append(0)
        for k in range(1, n + 1):
            a.append(l[k - 1] * k)
        m.append(sum(a))
        print(a)
    elif i == 2:
        for j in l:
            if j == 0:
                l.remove(0)
                l.insert((len(l)//2), j)
        for k in range(1, n + 1):
            a.append(l[k - 1] * k)
        m.append(sum(a))
        print(a)
print(max(m))'''

numberOfChildren = int(input())
preferences = list(map(int, input().split()))

childNumber = 0
preferenceSumStart = 0
for preference in preferences:
    if preference == 0:
        continue

    childNumber += 1
    preferenceSumStart += childNumber * preference

preferenceSumEnd = 0
maxPreferenceSum = preferenceSumStart + preferenceSumEnd
offsetChildIndex = numberOfChildren
for preference in reversed(preferences):
    preferenceSumStart -= offsetChildIndex * preference
    preferenceSumEnd += (offsetChildIndex + 1) * preference
    offsetChildIndex -= 1
    preferenceSum = preferenceSumStart + preferenceSumEnd
    maxPreferenceSum = max(preferenceSum, maxPreferenceSum)

print(maxPreferenceSum)