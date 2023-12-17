file = open('file.txt','w')
file.write('this is first line\nthis is second line\nthis is third line')
file.close()
lines = ['hi this is first line','this is second line','this is third line']
file1 = open('file1.txt','w')
for line in lines:
    file1.write(line+'\n')
file1.close()