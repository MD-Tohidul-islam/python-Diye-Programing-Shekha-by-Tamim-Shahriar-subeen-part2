import requests
img_url = 'http://goo.gl/jxktPw'
r = requests.get(img_url)
with open('pybook1.png','wb') as f:
    f.write(r.content)