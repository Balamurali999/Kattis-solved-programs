n = int(input())
a = bin(n).replace("0b", "")
a = a[::-1]
print(int(a, 2))
