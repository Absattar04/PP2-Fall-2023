a = [int(s) for s in input().split()]
x = int(input())
for i in range(x + 1, len(a)):
    a[i - 1] = a[i]
a.pop()
print(' '.join([str(i) for i in a]))