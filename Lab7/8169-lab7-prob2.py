class Name:
    def __init__(self, name, speed, maileage):
        self.name = name
        self.speed = speed
        self.maileage = maileage

class Car(Name):
    def __init__(self,vios,*arg):
        self.vios = vios
        super(Car, self).__init__(*arg)
        
    def set_speed(self, speed):
        self.speed = speed
    
    def __str__(self):
        return f"NAME: {self.name}  speed {self.speed} maileage {self.maileage} numdoor {self.vios}"

class Bus(Name):
    def __init__(self, volvo, *arg):
        self.volvo = volvo
        super(Bus, self).__init__(*arg)

    def set_speed(slef,speed):
        slef.speed = speed

    def __str__(self):
        return f"NAME: {self.name}  speed {self.speed} maileage {self.maileage} numdoor {self.volvo}"
class Car(Name):
    def __init__(self,vios,*arg):
        self.vios = vios
        super(Car, self).__init__(*arg)
        
    def set_speed(slef,speed):
        slef.speed = speed
    
    def __str__(self):
        return f"NAME: {self.name}  speed {self.speed} maileage {self.maileage} numdoor {self.vios}"
   
if __name__ == '__main__':
    car = Car("Toyota Vios", 98, 15000, 4)
    bus = Bus("School Volvo", 12 ,200000, 100)
    print(car)
    print(bus)
    bus.set_speed(30)
    print(bus)