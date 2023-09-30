x,z = [int(s) for s in input().split()]
bahn = ['I'] * x
for i in range(z):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        bahn[j] = '.'
print(''.join(bahn))