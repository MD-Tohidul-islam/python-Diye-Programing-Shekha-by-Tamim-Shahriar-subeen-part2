class Vehicle:
    '''Base clss for all vehicles'''

    def __init__(self,name,manufacturer,color):
        print('creating a vehicle')
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
    def drive(self):
        print('Driving',self.manufacturer,self.name)

class Car(Vehicle):
    """car class"""

    def __init__(self,name,manufacturer,color,year):
         print('creating a car')
         super().__init__(name,manufacturer,color)
         self.year = 2021
         self.wheels = 4
    def drive(self):
        super().drive()


if __name__ =='__main__':
    c = Car('tohidul 6.0It','Ford','red',2021)
    print(c.name,c.year,c.wheels)