import re
text = 'Email your feedback here: book@subeen.com py.book@subeen.com book_py@subeen.com thank you'
result = re.findall(r'\w+@\w+\.\w+',text)
print(result)
result1 = re.findall(r'[.\w]+@\w+\.\w+',text)
print(result1)