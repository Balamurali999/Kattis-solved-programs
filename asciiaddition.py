zero = [['xxxxx'], ['x...x'], ['x...x'], ['x...x'], ['x...x'], ['x...x'], ['xxxxx']]
one = [['....x'], ['....x'], ['....x'], ['....x'], ['....x'], ['....x'], ['....x']]
two = [['xxxxx'], ['....x'], ['....x'], ['xxxxx'], ['x....'], ['x....'], ['xxxxx']]
three = [['xxxxx'], ['....x'], ['....x'], ['xxxxx'], ['....x'], ['....x'], ['xxxxx']]
four = [['x...x'], ['x...x'], ['x...x'], ['xxxxx'], ['....x'], ['....x'], ['....x']]
five = [['xxxxx'], ['x....'], ['x....'], ['xxxxx'], ['....x'], ['....x'], ['xxxxx']]
six = [['xxxxx'], ['x....'], ['x....'], ['xxxxx'], ['x...x'], ['x...x'], ['xxxxx']]
seven = [['xxxxx'], ['....x'], ['....x'], ['....x'], ['....x'], ['....x'], ['....x']]
eight = [['xxxxx'], ['x...x'], ['x...x'], ['xxxxx'], ['x...x'], ['x...x'], ['xxxxx']]
nine = [['xxxxx'], ['x...x'], ['x...x'], ['xxxxx'], ['....x'], ['....x'], ['xxxxx']]
plus = [['.....'], ['..x..'], ['..x..'], ['xxxxx'], ['..x..'], ['..x..'], ['.....']]
n = []
for i in range(7):
    l = list(map(str, input().split()))
    n.append(l)
digits = []
for i in range(1,n+1):

