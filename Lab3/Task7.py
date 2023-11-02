a = [int(i) for i in input().split()]
x = int(input())
z = 0
while z < len(a) and a[z] >= x:
    z += 1
print(z + 1)