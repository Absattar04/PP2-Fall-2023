n = input().split()
x = set()
for i in n:
    if i in x:
        print('YES')
    else:
        print('NO')
    x.add(i)
