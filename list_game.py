n = int(input())
a = []
for i in range(2, n + 1):
    if n % i == 0:
        n = n / i
        a.append(i)
print(len(a))
