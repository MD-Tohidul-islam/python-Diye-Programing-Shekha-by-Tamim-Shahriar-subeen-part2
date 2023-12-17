import sys
print(sys.argv)
print(type(sys.argv))
print(f'the argument is {sys.argv[0]}')

arguments = sys.argv
a = arguments[1]
b = arguments[2]
print(a+b)
print(int(a)+int(b))

