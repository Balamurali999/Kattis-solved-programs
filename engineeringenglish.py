l = []
while True:
    try:
        n = str(input().split())
        l.extend(n)
        # Perform your operations
    except EOFError:
        # You can denote the end of input here using a print statement
        break

print(l)