num1 =  float(input("Enter a number : "))
num2 = float(input("Enter a number : "))
number = num1 + num2
print(f"{num1}+{num2} = {number}")

file = open("number.txt","w")
file.write(f"{num1}+{num2} = {number}")
file.close()

with open("number.txt","r") as readfile:
    print(readfile.read())