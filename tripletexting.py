n = str(input())
a = int(len(n)/3)
x = n[:a]
y = n[a:a*2]
z = n[a*2:a*3]
print(x) if x==y or x==z else print(y)
