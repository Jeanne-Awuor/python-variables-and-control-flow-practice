#Day of the Week Checker
#Python program that asks the user to enter a number (1 to 7)
# and prints the corresponding day of the week.
#If the number is outside the 1-7 range, print "Invalid input."
day=int(input("Enter a number: "))
#optimized function declaration
def day_checker(day):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# lists are zero-indexed ,so subtraction by 1 is necessary
    if 1 <= day <= 7:
        print(f"This is {days_of_week[day - 1]}")
        return days_of_week[day - 1]
    else:
        print("Invalid day! Please enter a number between 1 and 7.")


print(day_checker(day))