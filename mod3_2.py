"""define a class"""

class car:
    """create attributes of the class"""
    name = "Tesla"
    color = "White"
    price = 80000
    seat = "Leather"
    wheel = "Four"

    """define the class methods"""
    def get_name(self, name):
        self.name = name
        print(self.name)

    def get_color(self, color):
        self.color = color
        print(self.color)

    def get_price(self, price):
        self.price = price
        print(self.price)

    def get_seat(self, seat):
        self.seat = seat
        print(self.seat)

    def get_wheel(self, wheel):
        self.wheel = wheel
        print(self.wheel)

# creating an instance of the class
Car = car()

# calling the object methods
print(car.name)
print(car.color)
print(car.price)
print(car.seat)
print(car.wheel)
