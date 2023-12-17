def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('you can not divided by zero')
    except TypeError:
        print('Unsupported type. did you use string?')


print(div(3,4))
print(div(4,0))
print(div(8,4))

print(div('8',4))