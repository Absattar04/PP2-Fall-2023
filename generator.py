#1.Create a generator that generates the squares of numbers up to some number N.
def gen_squares(N):
    for i in range(N): 
        yield i**2
for x in gen_squares(10):
    print(x)

#2.Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def gen_even_num(N):
    for i in range(N+1):
        if i % 2 == 0:
            yield i
x = int(input())
y = gen_even_num(x)
for n in y:
    print(n)    

#3.Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def gen_divided(N):
    for i in range(N+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
a = int(input())
b = gen_divided(a)
for x in b:
    print(x)   

#4.Implement a generator called squares to yield the square of all numbers from (a) to (b). 
#Test it with a "for" loop and print each of the yielded values. 
def gen_squares(r,y):
    for i in range(r,y+1):
        yield i**2
a = int(input())
c = int(input())
b = gen_squares(a,c)
for n in b:
    print(n,end=' ')

#5.Implement a generator that returns all numbers from (n) down to 0.
def gen_return(x):
    for i in range(x, 0, -1):
        yield i
q = int(input())
e= gen_return(q)
for n in e:
    print(n, end = ' ')         