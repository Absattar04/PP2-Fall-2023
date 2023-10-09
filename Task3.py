a = input().split() 
b = input().split()
print(*sorted(set(a) & set(b),key = int))
