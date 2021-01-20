import requests
# r = requests.get('https://api.github.com/events')
# print(r.text)
# print(r.headers)
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('https://httpbin.org/post', data = payload)
print(r.url)
print(r.text)

