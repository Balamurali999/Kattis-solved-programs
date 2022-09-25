h, m = input().split()
h, m = int(h), int(m)
if h > 0:
    if m > 45:
        m -= 45
        print(f'{h} {m}')
    else:
        h -= 1
        m = (60-45)+m
        print(f'{h} {m}')
else:
    if m > 45:
        m -= 45
        print(f'{h} {m}')
    else:
        h = 23
        m = (60 - 45) + m
        print(f'{h} {m}')
