s = 'Afghanistan,America,Bangladesh,Canada,Denmark,England,Greenland,Iceland,Netherlands,New Zealand,Sweden, Switzerland'

country = s.split(',')
print(country)
print('....................................................................')
li = [item for item in country if item.endswith('land') or item.endswith('lands')]
print(li)
print('.............................................................')
import re
li1 = re.findall(r'\w+lands*',s)
print(li1)