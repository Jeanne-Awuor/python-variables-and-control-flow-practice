#Password Validator
# Python program that asks the user to enter a password.
# If the password is "python123",
#print "Access granted." Otherwise, print "Access denied."
password=input("Enter your password: ")
def password_checker(password):
    if password == "python123":
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")

print(password_checker(password))