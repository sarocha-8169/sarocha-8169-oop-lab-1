number = [1,2,3,4,5]
def add_number_to_list() :
    print(f"Before adding an integer, the list is {number} ")
    num = int(input("Enter the number to add to a list:"))
    number.append(num)
    print(f"After adding an integer {num}, the list is {number}")

def replace_number_in_list() :
    print(f"Finding a number to replace {number} ")
    findNum = int(input("Enter a number to find: "))
    replaceNum = int(input("Enter a new number to replace: "))
    for i in range(len(number)) :
        if number[i] == findNum :
            number[i] = replaceNum
    print(f"the list is {number}")

def remove_number_in_list() :
    print(f"Finding a number to remove the list is {number} ")
    removeNum = int(input("Enter a number to remove:"))
    number.remove(removeNum)
    print(f"the list is {number}")

if __name__ == "__main__":
    print(f"After adding an integer")
    add_number_to_list()
    replace_number_in_list()
    remove_number_in_list()
