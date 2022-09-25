x, w, h = input().split()
l = []
for i in range(int(x)):
    l.append(int(input()))
a = ((int(w)**2)+(int(h)**2))**(1/2)
for i in l:
    print('DA') if i <= a else print('NE')
