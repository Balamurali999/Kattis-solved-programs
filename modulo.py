l = []
for i in range(10):
    l.append(int(input()))
m = []
for i in l:
    m.append(i % 42)
print(len(set(m)))
