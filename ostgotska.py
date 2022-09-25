n = input().split()
c = 0
s = 0
for i in n:
    c += 1
    if 'ae' in i:
        s += 1
a = s/c
print('dae ae ju traeligt va') if a >= 0.4 else print('haer talar vi rikssvenska')
