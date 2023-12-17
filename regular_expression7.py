import re
text = 'multiple phone number, 017 11111111,01811111111,01911111111,01611111111,01511111111,123-123,00000000000'
result = re.findall(r'\d{3}\s*\d{8}',text)
print(result)
result1  =re.findall(r'01[56789]\s*\d{8}',text)
print(result1)