#1.Write a Python program to convert degree to radian.
degree = float(input("Input degree: "))
pi = 3.14
radian = degree*(pi/180)
print("Output radian: ",radian)

#2.Write a Python program to calculate the area of a trapezoid.
c = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))
S = 1/2*(a+b)*c 
print("Expected Output: ", S)

#3.Write a Python program to calculate the area of regular polygon.
import math
#pi = 3.14 
n = float(input("Input number of sides: "))
N = float(input("Input the length of a side: "))
S = (n * N**2) / (4 * math.tan(math.pi/n))
print("The area of the polygon is: ", S )

#4.Write a Python program to calculate the area of a parallelogram.
x = float(input("Length of base: "))
h = float(input("Height of parallelogram: "))
S = x * h
print("Expected Output: ", S)