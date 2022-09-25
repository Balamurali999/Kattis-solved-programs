n=int(input())
sr=[]
for i in range(n):
    a=int(input())
    sr.append(a)
sr=sr[::-1]
for i in range(len(sr)):
    print(sr[i])

