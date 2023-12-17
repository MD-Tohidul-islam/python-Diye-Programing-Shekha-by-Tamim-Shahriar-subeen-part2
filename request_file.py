import requests
url = 'http://subeen.com/allpost/'
response = requests.get(url)
print(response.ok)
print(response.status_code)
print(response.reason)
res = requests.get('http://example.com')
print(res.ok)
print(res.text)