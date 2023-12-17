import requests
img_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTr_MBnR0-H9yNbttikMln_tLajyCFX8xnBAA&usqp=CAU'
r = requests.get(img_url)
with open('pybook3.png','wb') as f:
    f.write(r.content)