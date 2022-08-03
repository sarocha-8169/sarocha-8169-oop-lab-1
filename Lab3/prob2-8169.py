fruits = ["Grapefruit", "Longan", "Orange", "Apple", "Cherry"] 
def orderFruit() :
    n = 0
    for i in range(len(fruits)):
        print(n+1,".",fruits[i])
        n+=1
    fruits.sort()

if __name__ == "__main__":
    print(f"The fruits are {fruits}") 
    print("After sorting fruits, fruits are")
    orderFruit()
    print(f"After sorting fruits, fruits are {fruits}")   