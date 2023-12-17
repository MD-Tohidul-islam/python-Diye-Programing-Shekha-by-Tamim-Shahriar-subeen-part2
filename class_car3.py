class Car:
    name = ''
    color = ''

    def start(self):
        print('starting car')

#creating a car class
my_car = Car()
your_car = Car()
my_car.name = 'allion'
my_car.color = 'gree'
your_car.name = 'bmw'
your_car.color = 'white'
print(my_car.name)
my_car.start()