n = list(map(str, input().split()))
print(max(int(n[0][::-1]), int(n[1][::-1])))
