# Simple Calculator with Conditionals
#a Python program that takes two numbers
# and an operation (+, -, *, /) from the user.
#Variable declaration
#user to be able to input any number
#user to be able to choose any operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operation (+, -, *, /): ")

 #function definition
def calculator(num1, num2, operator):
        if operator == "+":
            print(num1 + num2)
        elif operator == "-":
            print(num1 - num2)
        elif operator == "*":
            print(num1 * num2)
        elif operator == "/":
            print(num1/num2)

#results
print(calculator(num1, num2, operator))



