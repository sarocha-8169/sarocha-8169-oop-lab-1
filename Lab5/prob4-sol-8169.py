def get_operand(arg):
    correct_input = False
    while not correct_input:
        try:
            num = input(arg)
            if num == "q" or num == "Q":
                exit()
            nums = float(num)
        except ValueError:
            if num in 'Qq':
                break
            print("Please enter a valid decimal number")
        else:
            return nums


def get_operator(arg):
    operator1 = input(arg)
    return operator1


def get_format(answer):
    try:
        format1 = input("Enter output format(float, int): ")
        if format1 == "int":
            return int(answer)
        elif format1 is not None:
            if format1 == "" or format1 == "float":
                return float(answer)
            elif format1 == " ":
                print("Cannot devide by zero")
                print("We cannot perform your requested calculation")        
            
    except ValueError:
        pass


def robust_calculator(op1, op2, operator1):
    try:
        if operator1 == "+" or operator1 == "":
            result = op1 + op2
            # print("{} + {} = {}".format(op1,  op2, result))
            return result
        elif operator1 == "-":
            result = op1 - op2
            # print("{} - {} = {}".format(op1,  op2, result))
            return result
        elif operator1 == "*":
            result = op1 * op2
            # print("{} * {} = {}".format(op1,  op2, result))
            return result
        elif operator1 == "/":
            try:
                result = op1 / op2
                # print("{} / {} = {}".format(op1,  op2, result))
                return result
            except ZeroDivisionError:
                 
                pass       
    except ValueError:
        pass


def cal():
    while True:
        op1 = get_operand("Enter the first operand ('q' to quit): ")
        if op1 == "q" or op1 == "Q":
            break
        op2 = get_operand("Enter the second operand ('q' to quit): ")
        if op2 == "q" or op2 == "Q":
            break
        operator = get_operator("Enter an operation ('+','-','*','/'): ")
    
        if operator in "+-*/":
            ressult = robust_calculator(op1, op2, operator)
            get = get_format(ressult)
            if ressult is not None:
                print(f"{op1} {operator} {op2} = {get}")
            else:
                pass
            
        else:
            print("Operation must be '+','-','*','/'")
            pass


if __name__ == "__main__":
    cal()
