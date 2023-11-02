index = 0
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[index]:
        index = i
print(a[index], index)