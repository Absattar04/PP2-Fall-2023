n = int(input())
a = set(range(1, n + 1))
nums = a
while True:
    s = input()
    if s == 'HELP':
        break
    s = {int(x) for x in s.split()}
    if len(nums & s) > len(nums) / 2:
        print('YES')
        nums &= s
    else:
        print('NO')
        nums &= a - s
        
print(' '.join([str(x) for x in sorted(nums)]))
