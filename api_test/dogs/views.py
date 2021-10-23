from django.shortcuts import render
import requests


def index(request):
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    # print(type(r.text))  # str
    # print(r.json())  # dict
    r_json = r.json()
    message = r_json['message']
    context = {'image_url': message}
    print(message)
    return render(request, 'index.html', context)
