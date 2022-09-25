n = int(input())
b=[]
for i in range(n):
	l = list(map(int, input().split()))
	a = l.pop(0)
	s = sum(l)
	b.append(s-a+1)
for i in range(len(b)):
	print(b[i])