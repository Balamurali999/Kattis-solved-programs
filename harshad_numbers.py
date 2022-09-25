x = int(input())
while True:
    n = list(map(int, str(x)))
    if x % sum(n) == 0:
        print(x)
        break
    x += 1
