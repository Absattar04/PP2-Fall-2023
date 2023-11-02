#Task1
class String:
    def init_(s):
        s.string = ""

    def getString(s):
        s.string = input("Enter a string: ")

    def printString(s):
        print(s.string.upper())

m= String()
m.getString()
m.printString()

#Task2
class Shape:
    def init(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def init(self, length):
        self.length = length
    def area(self):
        return self.length ** 2
shape = Shape()
print(shape.area())  
square = Square(5)
print(square.area())    

#Task3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
rectangle = Rectangle(4, 6)
print(rectangle.area())          

#Task4
import math
class Point:
    def init(self, x, y, movedx, movedy):
        self.x = x
        self.y = y
        self.movedx = movedx
        self.movedy = movedy  
    def show(self):
        return( self.x, self.y)
    def move(self):
        self.movedx = self.movedx + self.x
        self.movedy = self.movedy + self.y
        return(self.movedx,self.movedy)
    def dist(self):
        return(math.sqrt((self.x - self.movedx)**2 + (self.y - self.movedy)**2))
point = Point(1, 2, 3, 3)
print(point.show())
print(point.move())
print(point.dist()) 

#Task5
class Account:
    def init(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into account. New balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal denied.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from account. New balance: {self.balance}")
            account = Account("John Doe", 1000)
account.deposit(500)  
account.withdraw(200)  
account.withdraw(2000)  

#Task6
def prime_num(y):
    x=0
    if(y==0 or y==1):
        return False
    for i in range(2,y):
        if y%i==0:
            x=x+1
    if x==0:
        return True
    else:
        return False
        
list_nums = [int(s) for s in input().split()]
primes = list(filter(lambda y:prime_num(y), list_nums))
for i in range(len(primes)):
    print(primes[i], end=' ')