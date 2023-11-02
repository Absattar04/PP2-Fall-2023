x = [int(i) for i in input().split()]
for i in range(1, len(x)):
    if x[i - 1] * x[i] >= 0:
        print(x[i - 1], x[i], end=' ')
        break