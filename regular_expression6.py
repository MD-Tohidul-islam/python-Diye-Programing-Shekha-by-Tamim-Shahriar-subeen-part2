import re
text0 = 'phone numeber: 01800000000'
phone_number = re.search('\d+',text0)
print(phone_number.group())
text1 = 'house number is : 5, phone number: 01700000000'

phone_number1 = re.search('\d+',text1)
print(phone_number1.group())
phone_number2 = re.search('\d{11}',text1)
print(phone_number2.group())
text2 = 'house number is : 5, phone number: 012 00000000'
phone_number3 = re.search('\d{3}\s*\d{8}',text2)
print(phone_number3.group())