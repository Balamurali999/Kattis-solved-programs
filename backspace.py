n=list(input())
l=[]
for i in n:
    if i=='<':
        l.pop()
    else:
        l.append(i)
print("".join(l))