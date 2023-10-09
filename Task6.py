a = int(input())
w = set()
for i in range(a):
    S = input().split()
    for elem in S:
        w.add(elem)
print(len(w))
