class Car:
    cc = '200'

    def __init__(self, name, color):  # name ane color are different from above name and color
        self.name = name
        self.color = color

    def start(self):
        print('starting car')


my_car = Car('corolla', 'red')
my_car.cc = 200
print(Car.cc)
print(my_car.name)
print(my_car.color)
print(my_car.cc)
your_car = Car('bmw','gree')
print(your_car.name)
my_car.start()
