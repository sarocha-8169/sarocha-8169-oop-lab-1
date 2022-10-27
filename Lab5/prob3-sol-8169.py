def get_number(msg):
    while True:
        try:
            num = int(input(msg))
            fact = 1
            if num >= 0:
                for i in range(1, num+1):
                    fact = fact*i
                print(fact)
                continue
            if num <= 0:
                print("Please enter an integer that is non-negative")
                break
            else:
                return num
        except ValueError:
            print("Please enter a valid integer!")
            break

input_int = get_number("Enter a non-negative integer:")