class Car:
    name = ''
    color = ''

    def start():
        print('starting car')

Car.name = 'Axio'
Car.color = 'black'
print('name of car: ',Car.name)
print('color of the car: ',Car.color)
Car.start()
