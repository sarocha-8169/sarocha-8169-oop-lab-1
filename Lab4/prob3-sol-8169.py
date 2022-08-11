def Covid_19():
    correct_input = False
    while not correct_input:
        try:
            negative = int(
                input("Enter the number of new infacted Covid19 cases for yesterday: "))
            print("Stay healthy!")
            while negative < 0:
                print("You can only enter a non-negative integer")
                print("Stay healthy!")
                negative = int(
                    input("Enter the number of new infacted Covid19 cases for yesterday: "))
                print("Stay healthy!")
            return negative
        except ValueError:
            print("Please enter a valid integer")
            print("Stay healthy!")


def Healthy_name():
    correct_input = False
    while not correct_input:
        try:
            positive = int(
                input("Enter the number of new infacted Covid19 cases for today: "))
            print("Stay healthy!")
            while positive < 0:
                print("You can only enter a non-negative integer")
                print("Stay healthy!")
                positive = int(
                    input("Enter the number of new infacted Covid19 cases for today: "))
                print("Stay healthy!")
            return positive
        except ValueError:
            print("Please enter a valid integer")
            print("Stay healthy!")


if __name__ == "__main__":
    negative = Covid_19()
    positive = Healthy_name()

    result = ((negative - positive)/negative) * 100
    results = abs(result)
    print(
        f"The difference of the number of new infacted cases is {results:.2f}%")