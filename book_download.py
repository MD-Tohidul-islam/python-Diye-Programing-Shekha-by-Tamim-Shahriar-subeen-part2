import requests
import sys

base_url = 'http://subeen.com/download/'
info_data = {'name':'Subeen',"email":'book@subeen.com','country':'Bangladesh'}

url = base_url+'process.php'
response = requests.post(url,data=info_data)
if response.ok is False:
    sys.exit('Error donwloading the file')
with open('cpbook.pdf','wb')as f :
    f.write(response.content)
print('Book donwload complete!')