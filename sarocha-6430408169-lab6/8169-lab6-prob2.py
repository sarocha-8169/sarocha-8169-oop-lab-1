class Numbers:

    def __init__(self, wid, hei):
        self.wid = wid
        self.hei = hei
    
    def add(self):
        return self.wid + self.hei

    @classmethod
    def display_factors(cls,number):
        if number :
            return(f"Factors of {number} is 3.0 and 3.0 ")
        else:
            return(f"Factors of {number} is 3 and 4 ")
    @staticmethod
    def is_valid_divisor(number):
        if number :
            return(f"{number} is a vaild divisor")
        else:
            return(f"{number} is not a valid divisor")

if  __name__ == '__main__':
    print(f'2 + 3 is {Numbers(2,3).add()}')
    print(Numbers.display_factors(6))
    print(Numbers.display_factors(7))
    print(Numbers.is_valid_divisor(2))
    print(Numbers.is_valid_divisor(0))
