import re
import requests
import sys

url = "http://dimik.pub"
responce = requests.get(url)
if responce.ok is False:
    sys.exit('Could not get response from server')

page_content = responce.text
regexp = re.compile(r'<div class="book-cover">\s*<a href="(.*?)">\s*<img src="(.*?)">.*?<h2 class="sd-title"><.*?>(.*?)<', re.S)
result = re.findall(regexp,page_content)
print(result)
print('we can see this resutl better than before\n ........\n......')
for item in result:
    print('Name:',item[2])
    print('Url:',item[0])
    print('Image:',item[1])
    print("")