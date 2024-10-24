#Triangle Type Checker
# Python program that takes the lengths of three sides of a triangle as input
#and determines if the triangle is:
#Equilateral (all sides are equal),
#Isosceles (two sides are equal), or
#Scalene (all sides are different).

#variable assignment
side1=float(input("Enter the side 1: "))
side2=float(input("Enter the side 2: "))
side3=float(input("Enter the side 3: "))

#function definition
def triangle_type_checker(side1,side2,side3):
    if side1 == side2 == side3:
        print("(Equilateral) The sides are equal")
    elif side1 == side2 or side2 == side3 or side3 == side1:
        print("(Isosceles) Two sides are equal")
    elif side1 != side3 and side3 != side2 and side1 != side2:
        print("(Scalene) No sides are equal")


print(triangle_type_checker(side1,side2,side3))
