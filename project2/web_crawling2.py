import re
import requests
url = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
resp = requests.get(url)
text = resp.text
text = text.replace("\n"," ")
book_pat = re.compile(r'<h3><a href="(.*?)" title="(.*?)">')
result = re.findall(book_pat,text)
print(len(result))
print(result[0])
next_page = re.findall(r'<li class="next"><a href="(.*?)">next</a></li',text)
print(next_page)
print(next_page[0])
