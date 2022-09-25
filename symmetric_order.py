while True:
    a = []
    n = int(input())
    for i in range(n):
        b = str(input())
        a.append(b)
    c = a.sort(key=len)
    for i in range(len(c)):
