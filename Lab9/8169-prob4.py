import sys

def compute(x):
    try:
        number = float(x)
        return number
    except ValueError:
        return None

if len(sys.argv) != 4:
    print(f"Usage python {sys.argv[0]} <operator> <operator1> <operator2>")
    exit(0)


operator = sys.argv[1]
operator1 = compute(sys.argv[2])
operator2 = compute(sys.argv[3])

try:
    if operator2 is None or operator1 is None:
        print("Operator are valid. They are not numbers")
        exit(0)
    
    if operator == '+':
        print (f'{operator1} {operator} {operator2} is {operator1 + operator2}')

    elif operator == '-':
        print (f'{operator1} {operator} {operator2} is {operator1 - operator2}')

    elif operator == '*':
        print (f'{operator1} {operator} {operator2} is {operator1 * operator2}')

    elif operator == '/':
        print (f'{operator1} {operator} {operator2} is {operator1 / operator2}')

    else:
        pass
except ZeroDivisionError:
    print(f'{operator1} cannot be divided by {operator2}')
