n = int(input())
l=[]
l[:0] = input()
m=[]
m[:0] = input()
if n % 2 == 1:
    for i in range(len(l)):
        if l[i] == '1':
            l[i] = '0'
        elif l[i] == '0':
            l[i] = '1'
print('Deletion succeeded') if l == m else print('Deletion failed')
