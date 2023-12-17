class Car:

    def __init__(self, name, color):  # name ane color are different from above name and color
        self.name = name
        self.color = color

    def start(self):
        print('starting car')


my_car = Car('corolla', 'red')
Car.start(my_car)