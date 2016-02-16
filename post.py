import requests


url = 'http://httpbin.org/post'
data = {'fname': 'Joseph', 'lname': 'Moran'}

post = requests.post(url, data=data)

print(post.content)