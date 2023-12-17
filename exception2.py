import io
file_name = 'file.txt'
mode = 'r'
try:
    with open(file_name,mode) as fp:
        content = fp.read()
        print(content)
except FileNotFoundError:
    print(file_name,'not found.please check if the file name')
except io.UnsupportedOperation:
    print('Are you sure',file_name,'is readable?')
    