student_ID = int(input("Please enter your student ID: "))
def score_(grade):
    if grade >= 80 :
        return "A"
    elif grade < 80 and grade >= 70 :
        return ("B")
    elif grade < 70 and grade >= 60 :
        return ("C")
    elif grade < 60 and grade >= 50 :
        return ("D")
    elif grade < 50 :
        return("F")
def get_first():
    while True:
        try:
            mid = float(input("Please enter the studet's midterm exam mark (0, 100): "))
            while mid < 0 or mid > 100 :
                print("Please enter a score in the range [0, 100]")
                mid = float(input("Please enter the studet's midterm exam mark (0, 100): "))
            return mid
        except ValueError:
            print("Please enter a score as a decimal number ")
def get_second_round():
    while True:
        try:
            final = float(input("Please enter the studet's final exam mark (0, 100): "))
            while final < 0 or final > 100 :
                print("Please enter a score in the range [0, 100]")
                final = float(input("Please enter the studet's final exam mark (0, 100): "))
            return final
        except ValueError:
            print("Please enter a score as a decimal number ")
mid = get_first()
final = get_second_round()
n = (final*(60/100) + mid*(40/100))
print(f"Student ID {student_ID} has the total mark as {n:.3f} has grade {score_(n)}",end=" ")