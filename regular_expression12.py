import re
s = 'Abcd 1234 - 33'
result = re.sub(r'\d','0',s)
print(result)
s1 = '22/07/2021,20/01/2021,01/01/2019'
new_s1 = re.sub(r'(\d{2})/(\d{2})/(\d{4})',r'\3-\2-\1',s1)
print(new_s1)
