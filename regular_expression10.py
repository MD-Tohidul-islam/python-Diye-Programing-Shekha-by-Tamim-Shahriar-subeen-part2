import re
s = '<li>Tamim</li><Shakib</li><li>Mahmidulla</li><li>Mominul</li>'
result1 = re.findall(r'<li>(.*?)</li>',s)
print(result1)