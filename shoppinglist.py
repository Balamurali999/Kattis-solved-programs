'''
a, b = list(map(int, input().split()))
l = []
for i in range(a):
    l.extend(list(map(str, input().split())))
m = []
c = 0
for i in range(len(l)-1):
    c = l.count(l[i])
    d = l.count(l[i+1])
    if c > d and c >= a:
        m.append(l[i])
    elif d > c and d >= a:
        m.append(l[i+1])

m = list(set(m))
print(len(m))

for i in m[::-1]:
    print("".join(i))
'''

'''
a, b = list(map(int, input().split()))
l = []
for i in range(a):
    l.extend(list(map(str, input().split())))
m = []
for i in l:
    if l.count(i) == a:
        m.append(i)
m = set(m)
print(len(m))
for i in m:
    print("".join(i))'''
numberOfLists, numberOfItems = list(map(int, input().split()))
isFirstList = True
recurringElements = set()
for _ in range(numberOfLists):
    shoppingElements = set(input().split())
    if isFirstList:
        isFirstList = False
        recurringElements.update(shoppingElements)
    else:
        recurringElements = recurringElements.intersection(shoppingElements)

sortedElements = sorted(recurringElements)
print(len(sortedElements))
for element in sortedElements:
    print(element)