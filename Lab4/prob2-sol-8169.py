def operation(number1, number2, operator):
   if operator == '+':
      return number1 + number2
   elif operator == '-':
      return number1 - number2
   elif operator == '*':
      return number1 * number2
   elif operator == '/':
      return number1 / number2

correct_input = False
while not correct_input:
   try:
        num1 = float(input("Enter the frist floating point number:"))
   except ValueError:
        print("Please enter a valid floating point number")
   else:
        correct_input = True

correct_input = False
while not correct_input:
   try:
       num2 = float(input("Enter the second floating point number:"))
   except ValueError:
      print("Please enter a valid floating point number:")
   else:
      correct_input = True

correct_input = False
while not correct_input:
   try:
      op = (input("Please enter operator (+, -, *, /):"))
      print(f"{num1} {op} {num2} = {operation(num1, num2, op)}")
   except ValueError:
      print("cannot divide by zero")
   else:
      correct_input = True
    
