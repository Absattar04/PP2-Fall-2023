#Task1
def grams_to_ounces(grams):
    print(28.3495231 * grams)
grams=float(input())
grams_to_ounces(grams)

#Task2
def Fin_C(F):
    print(float((5 / 9) * (F - 32)))
F=float(input())
Fin_C(F) 

#Task3
def solve(numheads, numlegs):
    kur = (numlegs - numheads*2 )/2
    rab = numheads - kur
    return rab , kur
print(solve(35,94))

#Task4
def primenums(n):
    a=0
    for i in range(2,n):
        if(n%i==0):
            a=a+1
    if(a==0):
        print(n,end=' ')
list = input().split()
for i in range(0, len(list)):
    primenums(int(list[i]))

#Task5
from itertools import permutations
def str_perm(str):
    w = permutations(str)
    for perm in w:
        print(''.join(perm))
x = input("Enter a string: ")
str_perm(x)

#Task6
def reverse_words(sentence):
    w = sentence.split()
    reversed_words = ' '.join(reversed(w))
    return reversed_words

user_input = input("Enter a sentence: ")
reversed_sentence = reverse_words(user_input)
print(f"The reversed sentence is: {reversed_sentence}")

#Task7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))  # True
print(has_33([1, 3, 1, 3]))  # False
print(has_33([3, 1, 3]))  # False

#Task8
def spy_game(nums):
    x = [0, 0, 7]
    i = 0
    for num in nums:
        if num == x[i]:
            i += 1
            if i == len(x):
                return True
    return False
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # False    

#Task9
import math
def sphery(r):
    return(float((4/3)* math.pi * r) )
r = int(input())
print(float(sphery(r)))

#Task10
def uniq_elements(list):
    l=[]
    for i in list: 
        if i not in l: 
            l.append(i) 
    return(l)
list = [int(s) for s in input().split()] 
res_list = uniq_elements(list)   
for i in res_list: 
    print(i, end=' ')

#Task11
def is_polindrome(s):
    if(s==s[::-1]):
        print("is polindrome")
    else:
        print("is not polindrome")
s=str(input())
is_polindrome(s)

#Task12
def histogram(numbers):
    for number in numbers:
        print('*' * number)
histogram([4, 9, 7])        

#Task13
import random
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print("Well, " + name + ", I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    guesses_taken = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            break
    print("Good job, " + name + "! You guessed my number in " + str(guesses_taken) + " guesses!")
guess_the_number()
