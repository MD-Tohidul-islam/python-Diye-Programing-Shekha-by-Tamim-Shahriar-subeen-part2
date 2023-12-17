import re
import requests
import sys
#url = 'http://books.toscrape.com/catalogue/the-exiled 247/index.html'
url = 'http://books.toscrape.com/catalogue/1000-places-to-see-before-you-die_1/index.html'
response = requests.get(url)
if response.ok is False:
    sys.exit('page could not get response')
page_content = response.text
page_content = page_content.replace("\n"," ")
regexp1 = re.compile(r'<div class="item active">\s*<img src="(.*?)"')
result1 = re.findall(regexp1,page_content)
print(result1)
regexp2 = re.compile(r'<div id="product_description" class="sub-header">.*?<p>(.*?)</p>')
result2 = re.findall(regexp2,page_content)
print(result2)
