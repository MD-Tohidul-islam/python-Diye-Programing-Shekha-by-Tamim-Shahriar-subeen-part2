
with open('file.txt','r') as fp:
    content1 = fp.read()
    print(content1)

with open('file1.txt','r') as f:
    lines = f.readline()
    print(lines)
    for line in lines:
        print(line)
print()
with open('file.txt','r')as f1:
    for line in f1:
        print(line)
with open('file3.txt','r') as f2:
    print(f2.read())