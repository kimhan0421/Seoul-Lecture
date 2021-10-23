import requests

r = requests.get('https://dog.ceo/api/breeds/image/random')

print(type(r.text))  # str
print(r.json())  # dict

r_json = r.json()
message = r_json['message']
print(message)
