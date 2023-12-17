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

class Car(Vehicle):
    def __init__(self,name,manufacture,color,year):
        self.name=name
        self.manufacture= manufacture
        self.color= color
        self.year = 2021
        self.wheels = 4
      

    def turn(self,direction):
        print(self.name,'is turning',direction)
    def change_gear(self,gear_name):
        '''method for changing gear'''

        print(self.name,'is changing gear to',gear_name)
if __name__=='__main__':
    c = Car('Mustaing 5.0 Gt couple','Ford','red',2017)
    v = Vehicle('sofia','davidson','blue')

    c.turn('right')
    v.turn('right')