class Cat:


    def __init__(self,name,color):
        self.name = name
        self.color = color



    def print_info(self):
        print(f"Cat name is {self.name} and its color is {self.color}")
    

    @classmethod
    def get_num_legs(cls):
        return 4


    @staticmethod
    def get_owner_name():
        return "Lalisa Manobal"


if __name__ == '__main__':
    num1 = Cat("Leo", "brown")
    num2 = Cat("Lily", "white")
    num1.print_info()
    num2.print_info()
    print(f"The number of legs of all cats is {Cat.get_num_legs()}")
    print(f"The owner of these cats is {Cat.get_owner_name()}")