import requests
import re
url = 'http://books.toscrape.com/index.html'
response = requests.get(url)
print(response.ok)
text = response.text
print(len(text))
result = re.findall(r'<div class="side_categories">(.*?)</div>',text,re.M|re.DOTALL)
print(len(result))
print('//////////....................')
print(type(result))
print('............')
print(result)
print('............./////////////')

category_path = re.compile(r'<li>\s*<a href="(.*?)">(.*?)<',re.M|re.DOTALL)
result1 = re.findall(category_path,text)
print(result1[0])
print('/////////???????????///////')
print(result1[1])
print('/////////////////...............')
category_path1 = re.compile(r'<li>\s*<a href="(.*?)">\s*(\w+[\s\w]+\w)\s*?<',re.M|re.DOTALL)
result2 = re.findall(category_path1,text)
print(result2[1])
print(len(result2))
