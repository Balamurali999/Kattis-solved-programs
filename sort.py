from collections import Counter

l = list(map(int, input().split()))
k = list(map(int, input().split()))

k = [n for n, count in Counter(k).most_common() for i in range(count)]

print(*k)