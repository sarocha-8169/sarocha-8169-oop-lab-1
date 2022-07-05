num1 =  float(input("Enter a number : "))
num2 = float(input("Enter a number : "))
number = num1 + num2
print(f"{num1}+{num2} = {number}")

print("Writing to my file numbers.txt")

file = open("number.txt","w")
file.write(f"{num1}+{num2} = {number}")
file.close()

print("Reading to my file numbers.txt")

with open("number.txt","r") as readfile:
    print(readfile.read())