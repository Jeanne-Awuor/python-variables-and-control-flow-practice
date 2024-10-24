#Grade Categorizer
#program that takes a score (0-100) as input
# and categorizes it into one of the following grades
# A (90-100)
# B (80-89)
# C (70-79)
# D (60-69)
# F (below 60)
score1=float(input("Enter your score: "))

def score_categorizer():
    if 100 <= score1 <= 90:
        print("A")
    elif 89 <= score1 <= 80:
        print("B")
    elif 79 <= score1 <= 70:
        print("C")
    elif 69 <= score1 <= 60:
        print("D")
    elif score1 < 60:
        print("F")

print(score_categorizer())
