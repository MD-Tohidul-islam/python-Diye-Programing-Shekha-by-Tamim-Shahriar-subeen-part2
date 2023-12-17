class some:

    def __init__(self, name, work, year):
        self.name = name
        self.work = work
        self.year = year

    def drive(self):
        print('drive')

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class Cat(some):

    def speak(self):
        print('mew')

class dog(some):
    def __init__(self,age,name,work,year):
        super().__init__(name, work, year)
        self.age = age
    def hi(self):
        print('hi')


c = Cat('bil','eat',2023)
c.speak()
c.drive()
d = dog(12,'ket','run',2021)
var = d.name
print(var)
# d = some('khan','sing',2021)
# d.set_name('razu')
# print(d.name)
# print(d.work)
d.hi()
d.drive()
