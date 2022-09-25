n = input().split()
a = int(n[0])
b = int(n[1])
c = int(n[2])
d = a%(b+c)
if b>d:
    print("Barb")
else:
    print("Alex")