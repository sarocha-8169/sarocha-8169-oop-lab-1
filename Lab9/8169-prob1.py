import re

my_info = "My name:Sarocha Phochaisri My ID is 6430408169"
search_str = re.split(":", my_info)
num_str = search_str[1]
num1 = re.search("[a-zA-Z]+.[a-zA-Z]+", num_str)
num2 = re.search("[My ID]\d.+", search_str[1])
print(f"My name is {num1.group()}")
print(f"My ID is{num2.group()}")

