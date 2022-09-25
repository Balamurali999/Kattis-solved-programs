while True:
    try:
        n = list(map(int, input().split()))
    except EOFError:
        break
    print(abs(n[0]-n[1]))