from django.shortcuts import render
import requests
from .models import DogImage


def index(request):
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    # print(type(r.text))  # str
    # print(r.json())  # dict
    r_json = r.json()
    message = r_json['message']

    dog_image, created = DogImage.objects.get_or_create(
        url=message,
        defaults={'urls': message}
    )
    print(f'{dog_image.url}-{created}')

    context = {'image_url': message}
    print(message)
    return render(request, 'index.html', context)
