# Odd or Even Checker
# Python program that asks the user for a number
# and then prints whether the number is odd or even.

num1= float(input("Enter number: "))
#function definition
def odd_or_even():
    if num1 % 2 == 0:
        print("This is an even number!!")
    else:
        print("This is an odd number!!")

print(odd_or_even())
