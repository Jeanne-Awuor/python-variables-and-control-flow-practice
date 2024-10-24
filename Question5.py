#Simple Age Checker
#Python program that asks the user for their age
# and tells them whether they are a minor,adult or senior
#(under 18), an adult (18-65), or a senior (over 65).
age=(float(input("Enter your age: ")))
def age_checker():
    if age < 18:
        print("You are a MINOR!!")
    elif age >= 18 and age < 65:
        print("You are a ADULT!!")
    else:
        print("You are a SENIOR!!")

print(age_checker())