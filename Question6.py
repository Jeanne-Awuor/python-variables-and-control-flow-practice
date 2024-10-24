#Password Validator
# Python program that asks the user to enter a password.
# If the password is "python123",
#print "Access granted." Otherwise, print "Access denied."

#variable assignment
password=input("Enter your password: ")
#function definition
def password_checker(password):
    if password == "python123":
        print("ACCESS GRANTED")
        return True
    else:
        print("ACCESS DENIED")
        return False
print(password_checker(password))