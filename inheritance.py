class Vehicle:
    '''parent class for all vehicle'''
    def __init__(self,name,manufacture,color):
        self.name = name
        self.manufacture = manufacture
        self.color = color

    def drive(self):
        print('Driving',self.manufacture,self.name)

    def turn(self,direction):
        print('Turning',self.name,'to',direction)

    def brake(self):
        print(self.name,'is stopping!')

if __name__=='__main__':
    v1 =Vehicle('Fusion 110 EX','Walton','Black')
    v2 = Vehicle('sofrail delux','harly_davidson','blue')

    # v1.drive()
    # v2.drive()
    #
    # v1.turn('left')
    # v2.turn('right')
    #
    # v1.brake()
    # v2.brake()

class Car(Vehicle):
    '''Car class'''

    def change_gear(self,gear_name):
        '''method for changing gear'''

        print(self.name,'is changing gear to',gear_name)
if __name__=='__main__':
    c = Car('Mustaing 5.0 Gt couple','Ford','red')
    c.drive()
    c.change_gear('p')
    c.brake()
