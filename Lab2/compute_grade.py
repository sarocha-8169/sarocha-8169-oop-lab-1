input
while True:
    try:
        num1 = float(input("Please enter your student ID : "))
        while num1 < 0 or num1 >10:
            print("Please enter a number in the range [0,10]")
            num1 = float(input("Please enter the first number:"))
        break
    except ValueError:
        print("Please enter a decimal number")

while True:
    try:
        num2 = float(input("Please enter the second number:"))
        while num2 < 0 or num2 > 10:
            print("Please enter a number in the range [0,10]") 
        break
    except ValueError:
        print("Please enter a decimal number")

avg = (num1 + num2) / 2
print(f'The average of {num1} and {num2} is {avg}')                   
               


