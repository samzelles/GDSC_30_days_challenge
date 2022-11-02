# Learning python basics
# GDSC 30 days challenge

# Personnal info class
class Personnal_info() :

    def __init__(self, name, address, age, phone) :
        self.name = name
        self.address = address
        self.age = age
        self.phone = phone

me = Personnal_info("Samuel", "Rue des Badamiers", 22, "98989898")
my_friend = Personnal_info("Florent", "Totsi", 25, "79999887")
my_second_friend = Personnal_info("Eli", "Totsi", 26, "97978999")

class Car() :
    def __init__(self, year_model, make, speed) :
        self.year_model = year_model
        self.make = make
        self.speed = speed


    def accelerate(self) :
        self.speed += 5


    def brake(self) :
        if self.speed >= 5 :
            self.speed -= 5
        
        if self.speed <= 0 :
            self.speed = 0
    
    def get_speed(self) :
        return self.speed


Range_rover = Car("2022", "", 200)
Range_rover.accelerate()
Range_rover.accelerate()
Range_rover.accelerate()
Range_rover.accelerate()
Range_rover.accelerate()

print(Range_rover.get_speed())

Range_rover.brake()
Range_rover.brake()
Range_rover.brake()
Range_rover.brake()
Range_rover.brake()

print(Range_rover.get_speed())
