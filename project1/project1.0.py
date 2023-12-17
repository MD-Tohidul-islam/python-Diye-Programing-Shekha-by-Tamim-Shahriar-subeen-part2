import re
text = 'Email your feedback here : book@subeen.com book@subeen thank you'
result = re.findall(r'(\w+@\w+.\w+)',text)
print(result)
result1 = re.findall(r'\w+@\w+\.\w+',text)
print(result1)
result2 = re.findall(r'\w+@\w+[.]\w+',text)
print(result2)