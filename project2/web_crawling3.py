import re
import requests
url ="http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
i = url.rfind("/")
print(url[0:i])
print(url[0:i+1])
url = url[0:i+1]+"page-2.html"
print(url)