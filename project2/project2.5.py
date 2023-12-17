import re
import p4
s=p4.result[6][0]
s1= 'http://dimik.pub/book/30/programming-career-guideline-by-tamim-shahriar-subeen">'
regex = re.compile(r'book/(\d+)/(\w+)-(\w+)-')
result1 = re.findall(regex,s1)
result2 = re.findall(regex,s)
print(result2)
print(result1)
li = list(result1[0])
print(li)
dir_name = '-'.join(li)
print(dir_name)