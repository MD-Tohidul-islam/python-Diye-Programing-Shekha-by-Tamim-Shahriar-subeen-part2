import turtle
class AjobTurtle2(turtle.Turtle):

    def forward(self, pixel):
        super().backward(pixel)

    def backword(self,pixel):
        super().forward(pixel)

    def left(self, angle):
        super().right(angle)
    def right(self,angle):
        print('I won\' turn right,because i am ajob😁')

if __name__ == '__main__':
    montu = AjobTurtle2()
    montu.right(40)
    montu.left(89)
    montu.forward(45)
    montu.left(42)
    montu.forward(34)
    montu.backward(32)

    jhonto = AjobTurtle2()
    jhonto.left(45)

    khan = turtle.Turtle()
    khan.shape('turtle')
    khan.left(30)
    khan.forward(200)
    khan.left(45)
    khan.backward(100)
    khan.right(90)
    khan.forward(10)

    turtle.done()