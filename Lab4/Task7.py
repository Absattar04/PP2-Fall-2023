x = int(input())
n = set(range(1, x + 1))
s = 0
while True:
    s = input()
    if s == "HELP":
        break
    else:
        a = set(list(map(int, s.split())))
        s = input()
        if s == "YES":
            n = n & a
        else:
            n = n - a
n = sorted(n)
print(*n)
